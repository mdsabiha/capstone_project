# 🧠 Hypertension Prediction Web App

This is a full-stack machine learning web application that predicts the likelihood of hypertension based on user input related to health and lifestyle. The model is trained using real-world health survey data and deployed using Flask.

---

## 🚀 Project Overview

Hypertension, or high blood pressure, is a critical health issue that often goes undetected. This project aims to:
- Identify key lifestyle and biological indicators influencing hypertension
- Predict the probability of an individual being hypertensive
- Provide an easy-to-use web interface for healthcare or personal use

---

## 🗂️ Repository Structure

```
├── __pycache__/                   # Cached Python files
├── static/                        # CSS, JS, or image files for frontend
├── templates/                     # HTML files (Flask views)
│   └── index.html                 # Main UI template
├── app.py                         # Flask application script
├── hypertension_model.pkl         # Trained machine learning model
├── logs.log                       # Application log file
├── requirements.txt               # Python dependencies
├── runtime.txt                    # Python version for deployment
├── Procfile                       # Heroku deployment instruction
└── README.md                      # Project documentation (this file)
```

---

## 📊 Features & Functionality

- 🧠 **Machine Learning Model**:
  - Trained using LightGBM, Random Forest, and AutoML (PyCaret)
  - Accuracy: ~86% with strong recall and AUC scores

- 📄 **Input Parameters**:
  - Age, Gender, Ethnicity
  - BMI, Waist Circumference
  - Glucose, Cholesterol, Smoking habits
  - Physical activity and sedentary time
  - Sodium, Potassium, Dietary fiber

- 🌐 **Web Application**:
  - Built with Flask (Python)
  - Simple, interactive HTML interface using Jinja2 templates
  - Displays prediction results on submission

---

## 🧪 Model Training Workflow (Summary)

- Data preprocessing & cleaning (handled in notebook)
- Feature engineering using domain knowledge
- EDA: Correlation heatmaps, distributions, and boxplots
- Model comparison via PyCaret
- Final model exported as `hypertension_model.pkl`

---

## ✅ How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hypertension-prediction-app.git
cd hypertension-prediction-app
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and go to `http://localhost:5000`.

---

## 🌐 Deployed Version

> 💡 Hosted on Heroku  
(https://capstone-project-kdj1.onrender.com/)
---

## 🧾 Sample Output

- **Prediction**: "You are likely to have Hypertension"  
- **Confidence Score**: 0.87  
- **Recommendations**: (optional placeholder for future integration)

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS (via `static/`), Jinja2 templates
- **Backend**: Flask, Python
- **ML Tools**: PyCaret, scikit-learn, LightGBM
- **Deployment**: Heroku (Procfile + runtime.txt)

---

## 📚 Future Enhancements

- Add charts/graphs to display insights dynamically
- Integrate patient history database
- Deploy with Streamlit for better UI/UX
- Add multilingual support

---

## 👨‍💻 Authors

**Group 6 – Capstone Team**  
- Harish Kumar Dakshinamoorthy  
- Sabiha Begum Mohammed  
- Sarath Krishna Marath  
- Nil Kumar G. Patel  
- Shreya Thakkar

---

## 📄 License

This project is licensed under the MIT License –
