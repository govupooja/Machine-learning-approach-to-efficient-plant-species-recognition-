import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

# Header for the app
st.header('Leaf Classification CNN Model')

# Define leaf names, scientific names, flowering seasons, and other details
leaf_names = ['Apple', 'Berry', 'Fig', 'Guava', 'Orange', 'Palm', 'Tomato']


# Additional details (for enhancing the output)
growth_habits = {
    'Apple': 'Tree-like',
    'Berry': 'Shrub',
    'Fig': 'Tree-like',
    'Guava': 'Shrub',
    'Orange': 'Tree',
    'Palm': 'Tree-like',
    'Tomato': 'Bushy'
}

climates = {
    'Apple': '15-24°C',
    'Berry': '12-22°C',
    'Fig': '18-30°C',
    'Guava': '20-30°C',
    'Orange': '20-30°C',
    'Palm': '18-30°C',
    'Tomato': '18-30°C'
}

soil_types = {
    'Apple': 'Well-drained, sandy loam',
    'Berry': 'Acidic, well-drained, sandy soil',
    'Fig': 'Loamy, well-drained soil',
    'Guava': 'Well-drained, sandy loam',
    'Orange': 'Well-drained, sandy loam',
    'Palm': 'Well-drained, sandy soil',
    'Tomato': 'Well-drained, loamy soil'
}

environmental_benefits = {
    'Apple': 'Helps absorb CO2, improves air quality, and provides habitat for pollinators.',
    'Berry': 'Acts as a carbon sink, helps reduce CO2 emissions, and supports biodiversity.',
    'Fig': 'Promotes carbon sequestration, improves soil fertility, and attracts pollinators.',
    'Guava': 'Helps improve soil quality, reduces erosion, and provides habitat for wildlife.',
    'Orange': 'Helps reduce air pollution, absorbs CO2, and supports biodiversity by attracting wildlife.',
    'Palm': 'Absorbs CO2, helps prevent desertification, and provides habitats for wildlife.',
    'Tomato': 'Promotes soil health, reduces soil erosion, and attracts beneficial insects.'
}


model = load_model(r'C:\Users\pooja\Downloads\Leaf classification\Leaf_classify.keras')

img_height = 180
img_width = 180

# Use file uploader to load the image
uploaded_file = st.file_uploader("Upload an image of a Flower", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Load and preprocess the image
        image = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(image)
        img_batch = tf.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        predictions = model.predict(img_batch)
        score = tf.nn.softmax(predictions[0])  # Get probabilities for each class

        # Get the predicted category
        predicted_class = leaf_names[np.argmax(score)]
        growth_habit = growth_habits[predicted_class]
        climate = climates[predicted_class]
        soil_type = soil_types[predicted_class]
        environmental_benefit = environmental_benefits[predicted_class]

        col1, col2 = st.columns([1, 2])  # Define two columns with ratio 1:2

        with col1:
            st.image(uploaded_file, caption="Uploaded Image", width=200)

        with col2:
            st.write(f"**Predicted Leaf:** {predicted_class}")
            st.write(f"**Growth Habit:** {growth_habit}")
            st.write(f"**Climate:** {climate}")
            st.write(f"**Soil Type:** {soil_type}")
            st.write(f"**Environmental Benefits:** {environmental_benefit}")
            st.write(f"**Confidence:** {np.max(score) * 100:.2f}%")

    except Exception as e:
        st.error(f"An error occurred while processing the image: {str(e)}")
else:
    st.write("Please upload an image to classify.")
