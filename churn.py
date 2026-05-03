import pickle 
import streamlit as st
import pandas as pd

with open('churn_model.pkl','rb') as file:
    model=pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

st.title("Customer Churn Prediction Model")
st.markdown("Churn Predictor")
st.write("Enter customer details to predict if they will churn or not")

col1 , col2=st.columns(2)


with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=3)

with col2:
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)
    num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=2)
    has_cr_card = st.selectbox("Has Credit Card?", [0, 1])
    is_active_member = st.selectbox("Is Active Member?", [0, 1])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

# Predict button
if st.button("Predict Churn"):
    # Prepare input data
    geo_encoded = {'Geography_Germany': 1 if geography == 'Germany' else 0,
                   'Geography_Spain': 1 if geography == 'Spain' else 0}
    
    gender_encoded = 1 if gender == 'Male' else 0
    

    input_data=pd.DataFrame({
        'CreditScore': [credit_score],
        'Gender': [gender_encoded],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary],
        'Geography_Germany': [geo_encoded['Geography_Germany']],
        'Geography_Spain': [geo_encoded['Geography_Spain']]
    })
    
    # Scale the input
    input_scaled = scaler.transform(input_data)
    
    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0]
    
    # Show result
    st.divider()
    if prediction[0] == 1:
        st.error("⚠️ Customer wILL Churn!")
    else:
        st.success("✅ Customer will NNOT Churn !")
    
    st.write(f"**Churn Probability:** {probability[1]*100:.2f}%")
    st.progress(probability[1])
