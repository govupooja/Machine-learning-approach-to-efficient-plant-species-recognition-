import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np

st.header('Fruit_Vegetable Recognition Model')

# Load the models
model = load_model(r'C:\Users\pooja\Downloads\Fruit_Vegetable classification\Image_classify.keras')


# Define class labels
fruits_veg = [
    'Apple', 'Banana', 'Beetroot', 'Bell Pepper', 'Cabbage', 'Capsicum', 'Carrot',
    'Cauliflower', 'Chilli Pepper', 'Corn', 'Cucumber', 'Eggplant', 'Garlic',
    'Ginger', 'Grapes', 'Jalepeno', 'Kiwi', 'Lemon', 'Lettuce', 'Mango', 'Onion',
    'Orange', 'Paprika', 'Pear', 'Peas', 'Pineapple', 'Pomegranate', 'Potato',
    'Raddish', 'Soy Beans', 'Spinach', 'Sweetcorn', 'Sweetpotato', 'Tomato',
    'Turnip', 'Watermelon'
]


details = {
    "Apple": {
        "benefits": "Rich in antioxidants, improves heart health, and aids digestion.",
        "vitamins": "Vitamin C, Vitamin K, Potassium"
    },
    "Banana": {
        "benefits": "Boosts energy, supports digestion, and aids in muscle recovery.",
        "vitamins": "Vitamin B6, Vitamin C, Magnesium"
    },
    "Beetroot": {
        "benefits": "Improves blood flow, reduces blood pressure, and boosts stamina.",
        "vitamins": "Vitamin C, Folate, Manganese"
    },
    "Bell Pepper": {
        "benefits": "Rich in antioxidants, improves eye health, and supports immunity.",
        "vitamins": "Vitamin C, Vitamin A, Vitamin E"
    },
    "Cabbage": {
        "benefits": "Improves digestion, supports heart health, and reduces inflammation.",
        "vitamins": "Vitamin K, Vitamin C, Folate"
    },
    "Capsicum": {
        "benefits": "Enhances metabolism, supports vision, and boosts immunity.",
        "vitamins": "Vitamin C, Vitamin B6, Vitamin A"
    },
    "Carrot": {
        "benefits": "Promotes eye health, supports skin health, and strengthens immunity.",
        "vitamins": "Vitamin A, Biotin, Vitamin K"
    },
    "Cauliflower": {
        "benefits": "Supports brain health, aids digestion, and boosts immunity.",
        "vitamins": "Vitamin C, Vitamin K, Folate"
    },
    "Chilli Pepper": {
        "benefits": "Boosts metabolism, reduces pain, and supports heart health.",
        "vitamins": "Vitamin C, Vitamin B6, Capsaicin"
    },
    "Corn": {
        "benefits": "Rich in fiber, improves vision, and supports digestion.",
        "vitamins": "Vitamin B1, Folate, Vitamin C"
    },
    "Cucumber": {
        "benefits": "Keeps you hydrated, supports skin health, and aids in weight loss.",
        "vitamins": "Vitamin K, Vitamin C, Potassium"
    },
    "Eggplant": {
        "benefits": "Supports brain function, improves heart health, and reduces blood sugar levels.",
        "vitamins": "Vitamin K, Vitamin C, Potassium"
    },
    "Garlic": {
        "benefits": "Boosts immunity, reduces blood pressure, and supports heart health.",
        "vitamins": "Vitamin C, Vitamin B6, Selenium"
    },
    "Ginger": {
        "benefits": "Reduces nausea, improves digestion, and helps fight inflammation.",
        "vitamins": "Vitamin B6, Magnesium, Manganese"
    },
    "Grapes": {
        "benefits": "Rich in antioxidants, improves heart health, and supports eye health.",
        "vitamins": "Vitamin C, Vitamin K, Potassium"
    },
    "Jalepeno": {
        "benefits": "Boosts metabolism, reduces pain, and supports heart health.",
        "vitamins": "Vitamin C, Vitamin B6, Capsaicin"
    },
    "Kiwi": {
        "benefits": "Rich in antioxidants, improves skin health, and boosts immunity.",
        "vitamins": "Vitamin C, Vitamin K, Vitamin E"
    },
    "Lemon": {
        "benefits": "Boosts immunity, aids digestion, and promotes skin health.",
        "vitamins": "Vitamin C, Potassium, Folate"
    },
    "Lettuce": {
        "benefits": "Supports hydration, improves digestion, and aids in weight loss.",
        "vitamins": "Vitamin K, Vitamin A, Folate"
    },
    "Mango": {
        "benefits": "Improves digestion, supports eye health, and boosts immunity.",
        "vitamins": "Vitamin A, Vitamin C, Vitamin E"
    },
    "Onion": {
        "benefits": "Boosts immunity, reduces inflammation, and supports heart health.",
        "vitamins": "Vitamin C, Vitamin B6, Manganese"
    },
    "Orange": {
        "benefits": "Boosts immunity, improves skin health, and supports heart health.",
        "vitamins": "Vitamin C, Folate, Potassium"
    },
    "Paprika": {
        "benefits": "Enhances metabolism, improves vision, and boosts immunity.",
        "vitamins": "Vitamin C, Vitamin A, Vitamin E"
    },
    "Pear": {
        "benefits": "Supports digestion, improves heart health, and promotes weight loss.",
        "vitamins": "Vitamin C, Vitamin K, Potassium"
    },
    "Peas": {
        "benefits": "Rich in protein, supports digestion, and improves heart health.",
        "vitamins": "Vitamin K, Vitamin C, Folate"
    },
    "Pineapple": {
        "benefits": "Reduces inflammation, supports digestion, and boosts immunity.",
        "vitamins": "Vitamin C, Vitamin B6, Manganese"
    },
    "Pomegranate": {
        "benefits": "Rich in antioxidants, improves heart health, and supports skin health.",
        "vitamins": "Vitamin C, Vitamin K, Folate"
    },
    "Potato": {
        "benefits": "Provides energy, supports digestion, and improves skin health.",
        "vitamins": "Vitamin C, Vitamin B6, Potassium"
    },
    "Raddish": {
        "benefits": "Improves digestion, supports detoxification, and reduces inflammation.",
        "vitamins": "Vitamin C, Folate, Potassium"
    },
    "Soy Beans": {
        "benefits": "Rich in protein, supports bone health, and improves heart health.",
        "vitamins": "Vitamin K, Folate, Iron"
    },
    "Spinach": {
        "benefits": "Rich in iron, supports eye health, and boosts immunity.",
        "vitamins": "Vitamin A, Vitamin C, Vitamin K"
    },
    "Sweetcorn": {
        "benefits": "Rich in fiber, supports digestion, and improves vision.",
        "vitamins": "Vitamin B1, Folate, Vitamin C"
    },
    "Sweetpotato": {
        "benefits": "Boosts immunity, supports eye health, and improves skin health.",
        "vitamins": "Vitamin A, Vitamin C, Potassium"
    },
    "Tomato": {
        "benefits": "Rich in antioxidants, improves skin health, and supports heart health.",
        "vitamins": "Vitamin C, Vitamin K, Potassium"
    },
    "Turnip": {
        "benefits": "Improves digestion, supports bone health, and boosts immunity.",
        "vitamins": "Vitamin C, Vitamin K, Folate"
    },
    "Watermelon": {
        "benefits": "Keeps you hydrated, improves heart health, and reduces inflammation.",
        "vitamins": "Vitamin A, Vitamin C, Potassium"
    }
}


img_height = 180
img_width = 180

# Use file uploader to load the image
uploaded_file = st.file_uploader("Upload an image of a fruit or vegetable", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    try:
        image = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(image)
        img_batch = tf.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        predictions = model.predict(img_batch)
        score = tf.nn.softmax(predictions[0])  # Get probabilities for each class

        # Get the predicted category and its details
        predicted_class = fruits_veg[np.argmax(score)]
        benefits = details[predicted_class]["benefits"]
        vitamins = details[predicted_class]["vitamins"]


        col1, col2 = st.columns([1, 2])

        # Display the uploaded image in the first column
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", width=200)

        # Display the prediction details in the second column
        with col2:
            st.write(f"**Predicted Item:** {predicted_class}")
            st.write(f"**Confidence:** {np.max(score) * 100:.2f}%")
            st.write(f"**Benefits:** {benefits}")
            st.write(f"**Rich Source:** {vitamins}")
    except Exception as e:
        st.error(f"An error occurred while processing the image: {str(e)}")
else:
    st.write("Please upload an image to classify.")

