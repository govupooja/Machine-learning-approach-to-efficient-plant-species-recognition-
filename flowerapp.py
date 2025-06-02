import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

st.header('Flower Classification CNN Model')

# Define flower names, scientific names, and flowering seasons
flower_names = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

scientific_names = {
    'Daisy': 'Bellis perennis',
    'Dandelion': 'Taraxacum officinale',
    'Rose': 'Rosa',
    'Sunflower': 'Helianthus annuus',
    'Tulip': 'Tulipa spp.'
}

flowering_seasons = {
    'Daisy': 'Late Spring to Early Fall',
    'Dandelion': 'Early Spring to Late Fall',
    'Rose': 'Late Spring to Fall',
    'Sunflower': 'Mid-Summer to Early Fall',
    'Tulip': 'Early to Late Spring'
}

# Load the pre-trained model
model = load_model(r'C:\Users\pooja\Downloads\Plant Classification Project\models\Flower_Recog_Model.keras')




def classify_images(image_path):
    # Load and preprocess the image
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)

    # Make predictions
    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    predicted_class = flower_names[np.argmax(result)]
    
    # Get the scientific name and flowering season for the predicted class
    scientific_name = scientific_names[predicted_class]
    flowering_season = flowering_seasons[predicted_class]
    
    # Get the confidence score
    confidence = np.max(result) * 100
    
    return predicted_class, scientific_name, flowering_season, confidence

# File uploader widget
uploaded_file = st.file_uploader('Upload an Image')
if uploaded_file is not None:
    # Save the uploaded file to the 'uploads' directory
    os.makedirs('upload', exist_ok=True)  # Ensure the upload directory exists
    with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Create two columns: one for the image and one for the details
    col1, col2 = st.columns([1, 2])  # The left column (1) is narrower, right column (2) is wider
    
    # Display the uploaded image in the left column
    with col1:
        st.image(uploaded_file, width=200)
    
    # Get classification results
    predicted_class, scientific_name, flowering_season, confidence = classify_images(uploaded_file)
    
    # Display the details in the right column
    with col2:
        st.write(f"**Flower Name**: {predicted_class}")
        st.write(f"**Scientific Name**: {scientific_name}")
        st.write(f"**Flowering Season**: {flowering_season}")
        st.write(f"**Confidence**: {confidence:.2f}%")
