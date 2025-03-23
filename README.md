# AI-Based-Medical-Diagnosis-Brain-Tumor-Detection

1. requirements.txt
This file includes all necessary dependencies for your Flask app, model inference, and front-end:

nginx
Copy
Edit
flask
tensorflow
numpy
pandas
scikit-learn
Pillow
matplotlib
gunicorn
werkzeug
If you're deploying on a cloud server, you might also need gunicorn for production.

2. README.md
Here’s a structured README.md for your GitHub repository:

markdown
Copy
Edit
# Brain Tumor Detection using ResNet-50 and Flask

This project is a web-based Brain Tumor Detection system that utilizes deep learning with **ResNet-50** for MRI image classification. The model is trained using TensorFlow and deployed using Flask.

## 📌 Features
- **Deep Learning Model:** Uses a pre-trained ResNet-50 model fine-tuned for MRI image classification.
- **Web Interface:** Allows users to upload MRI images for real-time tumor detection.
- **Flask Backend:** Handles image processing, model inference, and response generation.
- **Interactive UI:** Drag-and-drop & file upload functionality with a clean, modern design.

---

## 🚀 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/brain-tumor-detection.git
cd brain-tumor-detection
### 2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Flask App
sh
Copy
Edit
python app.py
The application will start, and you can access it in your browser at:

cpp
Copy
Edit
http://127.0.0.1:5000
📁 Project Structure
php
Copy
Edit
brain-tumor-detection/
│── static/                 # Static files (CSS, JavaScript, Images)
│── templates/              # HTML Templates
│   ├── index.html          # Main web interface
│── model/                  # Contains the trained model (.keras file)
│── app.py                  # Flask application
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
📸 Screenshots
Upload Image	Prediction Result
🧪 Testing
Upload an MRI scan image.

Click the Predict button.

The model will classify the tumor type.

🏗 Future Enhancements
Deploy on AWS/GCP for scalability.

Improve UI/UX for better user experience.

Extend model training with a larger dataset.

🤝 Contributing
Feel free to fork this repository and submit a pull request!


![Image](https://github.com/user-attachments/assets/cac04167-076f-48c2-8f47-8ccdf043bb6b)
