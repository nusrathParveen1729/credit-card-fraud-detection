import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("random_forest_model.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter 30 features to predict whether the transaction is fraudulent:")

# Input form
input_data = []
for i in range(1, 31):
    val = st.number_input(f"Feature {i}", step=0.01, format="%.4f")
    input_data.append(val)

if st.button("Predict"):
    input_array = np.array([input_data])
    prediction = model.predict(input_array)[0]
    
    if prediction == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✅ Transaction is Safe.")
