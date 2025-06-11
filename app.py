from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)  # Corrected __name__

model = tf.keras.models.load_model("D:/brain_tumor_app/model/final_brain_tumor_model.keras")
class_names = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]
SURVIVAL_INFO = {
    "Glioma": "Gliomas have an estimated 5-year survival rate of approximately 30–40%, depending on the grade.",
    "Meningioma": "Meningiomas generally have a favorable prognosis, with a 5-year survival rate exceeding 85%.",
    "No Tumor": "No brain tumor detected. No survival risk based on this MRI.",
    "Pituitary": "Pituitary tumors are often benign, with a survival rate of over 95% after treatment."
}

def predict(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = float(predictions[0][predicted_index])
    return predicted_class, confidence

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
        image = Image.open(file).convert("RGB")
        predicted_class, confidence = predict(image)
        survival_message = SURVIVAL_INFO.get(predicted_class, "Survival information not available.")

        return jsonify({
            "prediction": predicted_class,
            "confidence": f"{confidence:.2f}",
            "survival": survival_message
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":  # Corrected __name__
    app.run(debug=True)
