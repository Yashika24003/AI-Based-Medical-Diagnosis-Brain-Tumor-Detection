from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("D:\\brain_tumor_app\\model\\final_brain_tumor_model.keras")


# Define function to make predictions
def predict(image):
    img = image.resize((224, 224))  # Resize to model input size
    img = np.array(img) / 255.0     # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    predictions = model.predict(img)
    class_names = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]
    result = class_names[np.argmax(predictions)]
    return result

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        image = Image.open(file)
        result = predict(image)
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
