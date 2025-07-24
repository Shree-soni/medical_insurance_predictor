import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('model.pkl')

st.title("🏥 Medical Insurance Cost Predictor")

# Input fields
age = st.number_input("Age", 18, 100)
sex = st.selectbox("Sex", ['male', 'female'])         # 0 = male, 1 = female
bmi = st.number_input("BMI", 10.0, 50.0)
children = st.slider("Children", 0, 5)
smoker = st.selectbox("Smoker", ['yes', 'no'])        # 0 = yes, 1 = no
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])  # Encoded

# Encode input
sex = 0 if sex == 'male' else 1
smoker = 0 if smoker == 'yes' else 1
region_mapping = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}
region = region_mapping[region]

# Predict
if st.button("Predict"):
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Insurance Cost: ${prediction[0]:.2f}")
