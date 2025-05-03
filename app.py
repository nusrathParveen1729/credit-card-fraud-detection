from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    return "Credit Card Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read the JSON data
        data = request.get_json()
        input_df = pd.DataFrame([data])  # Turn dict into DataFrame
        prediction = model.predict(input_df)[0]

        return jsonify({'prediction': 'Fraud' if prediction == 1 else 'Not Fraud'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
