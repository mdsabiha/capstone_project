from flask import Flask, render_template, request
from pycaret.classification import load_model, predict_model
import pandas as pd

app = Flask(__name__)

# Load the saved PyCaret model
model = load_model('hypertension_model')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    input_data = pd.DataFrame([{
        'Age': float(request.form['age']),
        'Fasting_Glucose_mg_dL': float(request.form['glucose']),
        'BMI': float(request.form['bmi']),
        'LDL_Cholesterol': float(request.form['ldl']),
        'Triglycerides': float(request.form['triglycerides']),
        'Sedentary_Activity_Ratio': float(request.form['sedentary']),
        'Avg_Carb': float(request.form['carbs']),
        'Current_Diet': request.form['diet'],
        'Avg_Potassium': float(request.form['potassium']),
        'Avg_Calcium': float(request.form['calcium']),
    }])

    # Make prediction using the trained model
    result = predict_model(model, data=input_data)
    prediction = int(result['prediction_label'][0])

    # Generate personalized feedback based on inputs
    feedback = []

    # Example feedback based on user input
    if float(request.form['age']) > 50:
        feedback.append("As you're above 50, the risk of hypertension increases. Consider regular checkups.")
    if float(request.form['bmi']) > 30:
        feedback.append("Your BMI is on the higher side. This is one of the important factors for the risk of hypertension. Consider consulting a healthcare provider.")
    if float(request.form['glucose']) > 140:
        feedback.append("High fasting glucose level is associated with a higher risk of hypertension. Consider managing your glucose levels.")
    if float(request.form['sedentary']) > 5:  # Example threshold for sedentary activity ratio
        feedback.append("A high sedentary activity ratio increases the risk of hypertension. Try to stay more active.")
    if request.form['diet'] == "Weight Loss Diet":
        feedback.append("A weight loss diet can help in managing hypertension. Keep up the healthy eating habits!")

    # Return the result to the template with feedback
    return render_template('index.html', prediction=prediction, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
