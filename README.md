# Machine-learning-approach-to-efficient-plant-species-recognition-
🌿 Plant Classification System
An intelligent web-based application that identifies plants from images of flowers, fruits/vegetables, and leaves using deep learning. This solution combines Flask for backend management and Streamlit for a user-friendly interface. Built with TensorFlow and Convolutional Neural Networks (CNNs), it delivers fast and accurate plant species predictions along with educational insights.

🚀 Features
🌸 Classifies plant images based on flowers, fruits/vegetables, or leaves

🤖 Uses three separate CNN models trained with TensorFlow

📁 Allows users to upload images via Streamlit

🔁 Flask handles backend model integration and processing

📊 Provides additional plant information: habits, climate, and benefits

✅ Lightweight, fast, and easy to use

🌐 Accessible via web browser

🧠 Technologies Used
Tool/Library	Purpose
TensorFlow	Deep learning and model training
Keras	Simplified model building with CNNs
Streamlit	Interactive frontend for image input
Flask	Backend logic and routing
NumPy	Image preprocessing & array handling

📁 Project Structure
arduino
Copy
Edit
project/
│
├── models/
│   └── flower_model.keras
│   └── fruit_model.keras
│   └── leaf_model.keras
│
├── app/
│   └── app.py (Flask backend)
│   └── streamlit_app.py (Streamlit interface)
││
├── templates/
│   └── flindex.html
│   └── prediction.html
│   └── flcontact.html
│
├── uploads/ (for user image uploads)
├── README.md
└── requirements.txt
🧪 How It Works
User selects a plant part (flower, fruit/vegetable, or leaf)

Uploads an image through the Streamlit UI

The image is preprocessed and passed to the corresponding CNN model

Flask handles prediction and returns results

The user sees the predicted plant name, scientific name, confidence, and extra info

🌱 Use Cases
Home gardening assistance

Agriculture and crop management

Botany education and plant awareness

Eco-awareness campaigns

🔧 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/plant-classification-system.git
cd plant-classification-system

# Install dependencies
pip install -r requirements.txt

# Run the Flask server (if needed)
python app/app.py

# Or launch the Streamlit interface directly
streamlit run app/streamlit_app.py
📷 Example
<img src="demo/sample_upload.png" width="300"> _Result: Rose - Scientific Name: Rosa - Confidence: 97.6%_
