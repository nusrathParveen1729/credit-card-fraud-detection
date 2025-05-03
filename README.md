##💳 -  Card Fraud Detection ##
A machine learning-based web application that detects fraudulent credit card transactions using a Random Forest Classifier. This project includes model training, scaling, and deployment using both Flask API and Streamlit UI.


## Features ##
This project is designed to detect fraudulent transactions using anonymized credit card transaction data. It leverages a Random Forest Classifier trained on a dataset containing 30 input features. 
To ensure consistent performance, all features are scaled using StandardScaler during both training and inference. The application provides two modes of access: a RESTful API built with Flask for
backend interaction, and a user-friendly web interface developed using Streamlit. Additionally, it includes a simple test script (test_request.py) to simulate and verify API predictions with ease.


## Model ##
Algorithm: Random Forest Classifier
Input: 30 scaled features per transaction
Output: Binary classification — Fraud or Not Fraud


## Dependencies ##
scikit-learn
pandas
numpy
flask
streamlit
joblib


## Notes ##
Ensure that the input to the model has exactly 30 features after scaling.
The model will raise an error if input dimensions are incorrect.

## Acknowledgments ##
Dataset from Kaggle: Credit Card Fraud Detection
Streamlit and Flask communities

