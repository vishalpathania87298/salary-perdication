import streamlit as st
import numpy as np
import pandas as pd
import joblib
st.set_page_config(page_title="Salary_Prediction_",layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("Salary_Prediction_Model.joblib")

model=load_model()
st.title("salary prediction ")
st.write("Enter the  experience year of employ and get prediction of salary")

Experience=st.number_input("year Experience ",min_value=0.0)


if st.button("Predict salary"):
    try:
        input_data=np.array([[Experience]])
        prediction=model.predict(input_data)
        st.success(f"Predicted Performance Index **{prediction[0]}**")
    except Exception as e:
        st.error("Error!!!!!!!!!!")