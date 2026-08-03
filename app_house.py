import streamlit as st
import pickle
import os
import time
#------------------------
#CACHING EXAMPLE
#------------------------
@st.cache_resource
def load_model():
    if not os.path.exists("house_price_model.pkl"):
        raise FileNotFoundError("Model file not found")
    with open("house_price_model.pkl","rb")as file:
        model = pickle.load(file)
    return model
if "prediction_count"not in st.session_state:
    st.session_state.prediction_count=0
st.title("House price prediction")
#----------------------
#LOAD MODEL
#--------------------
try:
    model = load_model()
except Exception as e:
    st.error(e)
    st.stop()
    #----------------------
    #INPUTS
    #----------------------
area = st.number_input("Area(sq.ft)",1000,5000,1500)
bedrooms = st.slider("Bedrooms",1,10,3)
age = st.slider("House Age",0,30,5)

#--------------------
#PREDICTION
#--------------------
if st.button("Predict here"):
    try:
        prediction = model.predict([[area,bedrooms,age]])
        st.success(f"Estimated price : {prediction[0]:,.0f}")
        st.session_state.prediction_count+=1
    except Exception as e:
        st.error("Prediction Failed")
        st.exception(e)

    #------------------------
    #SESSION STATE DEMO
    #------------------------
    st.info(f"Predictions made: {st.session_state.prediction_count}")

    #------------------------
    #RESET SESSION
    #-------------------------
    if st.button("Reset counter"):
        st.session_state.prediction_count=0
        st.success("Counter reset")