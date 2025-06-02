from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the home page with options

def streamlit_app():
    # Replace with the URL where your Streamlit app is running
    return redirect("http://127.0.0.1:8101")

def streamlit_app():
    # Replace with the URL where your Streamlit app is running
    return redirect("http://127.0.0.1:8102")

def streamlit_app():
    # Replace with the URL where your Streamlit app is running
    return redirect("http://127.0.0.1:8103")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=2003)  # Explicitly set host to 127.0.0.1
