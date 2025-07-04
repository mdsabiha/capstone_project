# 🩺 Hypertension Prediction Using Lifestyle and Health Data

This project focuses on predicting hypertension using lifestyle patterns, demographic details, and health-related indicators. It aims to help understand risk factors and build a reliable machine learning model for early detection and prevention of hypertension.

---

## 📌 Project Objective

Hypertension (high blood pressure) is a silent yet critical health concern affecting millions worldwide. This project leverages health data to:
- Analyze and identify factors contributing to hypertension
- Build predictive models using machine learning algorithms
- Provide interpretable results to aid healthcare professionals and researchers

---

## 📁 Repository Structure

```
hypertension-prediction/
├── Group_6(Hypertension_Prediction).ipynb     # Main Jupyter Notebook
├── README.md                                  # Project documentation (this file)
├── LICENSE                                    # MIT License (if included)
└── data/                                      # Folder for datasets (optional)
```

---

## 🧬 Dataset Description

The dataset includes both numerical and categorical health indicators, sourced from public health survey data. Key features include:
- **Demographics**: Age, Gender, Ethnicity, Education, Income
- **Health Metrics**: Blood pressure, BMI, Waist Circumference, Glucose, Cholesterol
- **Dietary Intake**: Sodium, Potassium, Fiber, Fats, Vitamins
- **Lifestyle**: Smoking status, Physical activity (moderate/vigorous), Sedentary time

---

## 🧠 ML Workflow

1. **Data Preprocessing**
   - Missing value handling
   - Label encoding and normalization
   - Creation of derived columns (e.g., average BP, age groups)

2. **Exploratory Data Analysis (EDA)**
   - Distribution plots and boxplots
   - Correlation heatmaps
   - Crosstabs and group comparisons

3. **Modeling**
   - Logistic Regression
   - Random Forest
   - LightGBM
   - AutoML with PyCaret

4. **Evaluation**
   - Accuracy, Precision, Recall, F1-score
   - Confusion Matrix
   - ROC-AUC Curve

5. **Interpretability**
   - Feature importance analysis
   - SHAP-based interpretation (optional)

---

## 📊 Key Insights

- **BMI, Waist Circumference, and Glucose levels** are strong predictors of hypertension.
- High **sodium intake** and **low fiber** consumption correlate with elevated BP risk.
- **Physical inactivity** and **smoking** show a significant impact on hypertension rates.
- **Random Forest** and **LightGBM** yielded the best results with >85% accuracy.

---

## 🔬 Tools & Technologies

- Python
  - Pandas, NumPy, Scikit-learn
  - Matplotlib, Seaborn
  - PyCaret, LightGBM
- Jupyter Notebook
- Microsoft Excel / Power BI (optional for data exploration)

---

## 📈 Evaluation Metrics

- **Confusion Matrix**: To visualize TP/FP/FN/TN
- **F1 Score**: To handle class imbalance
- **ROC-AUC**: To measure classifier performance
- **Precision/Recall**: For medical prediction relevance

---

## 👥 Team Members

This project was developed by **Group 6 – Capstone Team**:
- Harish Kumar Dakshinamoorthy  
- Sabiha Begum Mohammed  
- Sarath Krishna Marath  
- Nil Kumar G. Patel  
- Shreya Thakkar

---

## 🪪 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✅ How to Run

1. Clone the repository
2. Open `Group_6(Hypertension_Prediction).ipynb` in Jupyter Notebook
3. Execute the cells in sequence to view EDA, modeling, and evaluation outputs

---

## 💡 Future Improvements

- Integrate a live dashboard (e.g., Streamlit or Power BI)
- Expand dataset with time-series or longitudinal data
- Implement model deployment via API
