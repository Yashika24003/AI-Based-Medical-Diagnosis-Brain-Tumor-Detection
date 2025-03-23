# AI-Based-Medical-Diagnosis-Brain-Tumor-Detection

# Brain Tumor Detection using ResNet-50 and Flask

This project is a web-based Brain Tumor Detection system that utilizes deep learning with **ResNet-50** for MRI image classification. The model is trained using TensorFlow and deployed using Flask.

**📌 Features**
- **Deep Learning Model:** Uses a pre-trained ResNet-50 model fine-tuned for MRI image classification.
- **Web Interface:** Allows users to upload MRI images for real-time tumor detection.
- **Flask Backend:** Handles image processing, model inference, and response generation.
- **Interactive UI:** Drag-and-drop & file upload functionality with a clean, modern design.

---

**🚀 Installation**

**1️⃣ Clone the Repository**
```sh
git clone https://github.com/Yashika242003/brain-tumor-detection.git
cd brain-tumor-detection
```

**2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
**requirements.txt**
This file includes all necessary dependencies for your Flask app, model inference, and front-end:
flask
tensorflow
numpy
pandas
scikit-learn
Pillow
matplotlib

```
**3️⃣ Run the Flask App**
```sh
python app.py
```

The application will start, and you can access it in your browser at:
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure
```
brain-tumor-detection/
│── static/                 # Static files (CSS, JavaScript, Images)
│── templates/              # HTML Templates
│   ├── index.html          # Main web interface
│── model/                  # Contains the trained model (.keras file)
│── app.py                  # Flask application
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```

---

## 📸 Screenshots

![Image](https://github.com/user-attachments/assets/cac04167-076f-48c2-8f47-8ccdf043bb6b)

---

## 🧪 Testing
- Upload an MRI scan image.
- Click the **Predict** button.
- The model will classify the tumor type.

---

## 🏗 Future Enhancements
- Deploy on **AWS/GCP** for scalability.
- Improve UI/UX for better user experience.
- Extend model training with a larger dataset.

---


