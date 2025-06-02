from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Allowed file extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Set the folder for file uploads
app.config['UPLOAD_FOLDER'] = 'leuploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page
@app.route('/')
def home():
    return render_template('leindex.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('lecontact.html')

# Prediction page
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Check if an image is part of the request
        if 'image' not in request.files:
            return redirect(request.url)
        
        file = request.files['image']
        
        # If a valid image is uploaded
        if file and allowed_file(file.filename):
            # Save the file
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Simulated prediction logic
            # Replace this with your actual model prediction logic
            confidence = 0.45  # Placeholder confidence value (modify as needed)
            if confidence < 0.50:  # Threshold for valid classification
                # Redirect back to the prediction page without result
                return redirect(url_for('prediction'))
            
            # Show the result on the prediction page
            predicted_item = "Apple"  # Placeholder predicted item
            return render_template(
                'prediction.html', 
                filename=filename, 
                predicted_item=predicted_item, 
                confidence=confidence * 100, 
                growth_habits ="Tree-like",
                climates ="15-24°C",
                soil_types = "Well-drained, sandy loam",
                environmental_benefits ="Absorbs CO2, improves air quality, and provides habitat for pollinators."
            )
    
    return render_template('prediction.html', filename=None)

# Streamlit app redirection
@app.route('/streamlit_app')
def streamlit_app():
    # Replace with the URL where your Streamlit app is running
    return redirect("http://localhost:8503")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8104, debug=False)
