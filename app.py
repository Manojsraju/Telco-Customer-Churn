import streamlit as st
import pandas as pd
import pickle

# Load model
with open('pipeline_xgb.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Customer Churn Prediction")

st.write("Enter customer details below")

# Inputs
gender = st.selectbox("Gender", ['Male', 'Female'])

seniorcitizen = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ['Yes', 'No'])

dependents = st.selectbox("Dependents", ['Yes', 'No'])

tenure = st.number_input("Tenure", min_value=0)

phoneservice = st.selectbox("Phone Service", ['Yes', 'No'])

multiplelines = st.selectbox(
    "Multiple Lines",
    ['Yes', 'No', 'No phone service']
)

internetservice = st.selectbox(
    "Internet Service",
    ['DSL', 'Fiber optic', 'No']
)

onlinesecurity = st.selectbox(
    "Online Security",
    ['Yes', 'No', 'No internet service']
)

onlinebackup = st.selectbox(
    "Online Backup",
    ['Yes', 'No', 'No internet service']
)

deviceprotection = st.selectbox(
    "Device Protection",
    ['Yes', 'No', 'No internet service']
)

techsupport = st.selectbox(
    "Tech Support",
    ['Yes', 'No', 'No internet service']
)

streamingtv = st.selectbox(
    "Streaming TV",
    ['Yes', 'No', 'No internet service']
)

streamingmovies = st.selectbox(
    "Streaming Movies",
    ['Yes', 'No', 'No internet service']
)

contract = st.selectbox(
    "Contract",
    ['Month-to-month', 'One year', 'Two year']
)

paperlessbilling = st.selectbox(
    "Paperless Billing",
    ['Yes', 'No']
)

paymentmethod = st.selectbox(
    "Payment Method",
    [
        'Electronic check',
        'Mailed check',
        'Bank transfer (automatic)',
        'Credit card (automatic)'
    ]
)

monthlycharges = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

totalcharges = st.number_input(
    "Total Charges",
    min_value=0.0
)

# Feature Engineering
avgcharges = totalcharges / (tenure + 1)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame({

        'gender': [gender],
        'seniorcitizen': [seniorcitizen],
        'partner': [partner],
        'dependents': [dependents],
        'tenure': [tenure],
        'phoneservice': [phoneservice],
        'multiplelines': [multiplelines],
        'internetservice': [internetservice],
        'onlinesecurity': [onlinesecurity],
        'onlinebackup': [onlinebackup],
        'deviceprotection': [deviceprotection],
        'techsupport': [techsupport],
        'streamingtv': [streamingtv],
        'streamingmovies': [streamingmovies],
        'contract': [contract],
        'paperlessbilling': [paperlessbilling],
        'paymentmethod': [paymentmethod],
        'monthlycharges': [monthlycharges],
        'totalcharges': [totalcharges],
        'avgcharges': [avgcharges]

    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:

        st.error("Customer is likely to churn")

    else:

        st.success("Customer is likely to stay")
