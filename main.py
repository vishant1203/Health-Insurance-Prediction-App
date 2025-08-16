import streamlit as st
import numpy as np
from prediction_helper import predict

#--Title
st.title("Health Insurance Premium Prediction App(Vishant)")


col1, col2, col3=st.columns(3)
col4, col5, col6=st.columns(3)
col7, col8, col9=st.columns(3)
col10, col11, col12=st.columns(3)
col13,col14, col15=st.columns(3)

with col1:
    Age = st.number_input("Age", min_value=0, max_value=120, value=30)
with col2:
    Gender = st.selectbox("Gender", ['Male', 'Female'])
with col3:
    Region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
with col4:
    Marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
with col5:
    BMI_Category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
with col6:
    Smoking_Status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])
with col7:
    Employment_Status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer', 'NA'])
with col8:
    Income_Level = st.selectbox("Income Level", ['<10L', '10L - 25L', '> 40L', '25L - 40L', 'NA'])
with col9:
    Medical_History = st.selectbox("Medical History", [
    'Diabetes', 'High blood pressure', 'No Disease',
    'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
    'High blood pressure & Heart disease', 'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ])
with col10:
    Insurance_Plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])
with col11:
    Number_Of_Dependants = st.number_input("Number of Dependants", min_value=0, value=0)
with col12:
    Income_Lakhs = st.number_input("Income (Lakhs)", min_value=0.0, value=5.0)
with col13:
    Genetical_Risk = st.number_input("Genetical Risk", min_value=0, max_value=100, value=1)

input_data = {
        'Gender': Gender,
        'Region': Region,
        'Marital_status': Marital_status,
        'BMI_Category': BMI_Category,
        'Smoking_Status': Smoking_Status,
        'Employment_Status': Employment_Status,
        'Income_Level': Income_Level,
        'Medical_History': Medical_History,
        'Insurance_Plan': Insurance_Plan,
        'Age': Age,
        'Number_Of_Dependants': Number_Of_Dependants,
        'Income_Lakhs': Income_Lakhs,
        'Genetical_Risk': Genetical_Risk
    }

if st.button("Calculate Premium"):
    prediction=predict(input_data)
    st.success(f'Predicted Heath insurance cost: {prediction}')



