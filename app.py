import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
#from plotly.subplots import make_subplots
#import plotly.graph_objects as go
#import matplotlib.pyplot as plt
#import seaborn as sns
import pickle
from PIL import Image

image = Image.open('logo.png')

st.image(image, caption='')

pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

pickle_m = open('logisticRegr_male.pkl', 'rb')
classifier_m = pickle.load(pickle_m)

#st.sidebar.header('Diabetes Prediction for females above 21 years')
#select = st.sidebar.selectbox('Select Form', ['Unhide to proceed'], key='1')
#if not st.sidebar.checkbox("Hide", True, key='2'):
tab1, tab2, tab3 = st.tabs(["Male", "Female","Glossary"])
#st.header("Choose your Gender to proceed")
with tab1:
   st.header("Welcome to Our Diabetes Prediction App")
   #st.divider()
   st.header(':red[_Diabetes Prediction(Only for males above 21years of age)_]')
   glucose = st.slider("Plasma Glucose Concentration :",0,199,1); st.caption(":red[_Input between 0 to 199_]")
   bp =  st.slider("Diastolic blood pressure (mm Hg)",0,122,1); st.caption(":red[_Input between 0 to 122_]")
   skin = st.slider("Triceps skin fold thickness (mm):",0,99,1); st.caption(":red[_Input between 0 to 99_]")
   insulin = st.slider("2-Hour serum insulin (mu U/ml):",0,846,1); st.caption(":red[_Input between 0 to 846_]")
   bmi = st.slider("Body mass index (weight in kg/(height in m)^2):",0.00,67.1,0.1); st.caption(":red[_Input between 0 to 67.1_]")
   dpf = st.slider("Diabetes Pedigree Function:",0.00,2.42,0.1); st.caption(":red[_Input between 0 to 2.42_]")
   age = st.number_input("Age:",key='3')
   submit = st.button('Predict',key='5')
   if submit:
        prediction = classifier_m.predict([[glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write(':blue[Congratulation','You are not diabetic]')
            st.caption(":red[_NB: The dataset used for this study is PIMA Indian Diabetes Dataset from Kaggle_]")
        else:
            st.write(" :red[_We are really sorry to say but it seems like you are Diabetic_]")
            st.caption(":red[_NB: The dataset used for this study is PIMA Indian Diabetes Dataset from Kaggle_]")

with tab2:
   st.header("Welcome to Our Diabetes Prediction App")
   #st.divider()
   #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   st.header(':red[_Diabetes Prediction(Only for females above 21years of age)_]')
    #name = st.text_input("Name:")
   pregnancy = st.number_input("No. of times pregnant:");  st.caption(":red[_Input between 0 to 17_]")
   glucose = st.number_input("Plasma Glucose Concentration :"); st.caption(":red[_Input between 0 to 199_]")
   bp =  st.number_input("Diastolic blood pressure (mm Hg):"); st.caption(":red[_Input between 0 to 122_]")
   skin = st.number_input("Triceps skin fold thickness (mm):"); st.caption(":red[_Input between 0 to 99_]")
   insulin = st.number_input("2-Hour serum insulin (mu U/ml):"); st.caption(":red[_Input between 0 to 846_]")
   bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):"); st.caption(":red[_Input between 0 to 67.1_]")
   dpf = st.number_input("Diabetes Pedigree Function:"); st.caption(":red[_Input between 0 to 2.42_]")
   age = st.number_input("Age:")
   submit = st.button('Predict')
   if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write(':blue[Congratulation','You are not diabetic]')
            st.caption(":red[_NB: The dataset used for this study is PIMA Indian Diabetes Dataset from Kaggle_]")
        else:
            st.write(" :red[_We are really sorry to say but it seems like you are Diabetic_]")
            st.caption(":red[_NB: The dataset used for this study is PIMA Indian Diabetes Dataset from Kaggle_]")
with tab3:
    with st.expander("Body Mass Index"):
        st.write("Body Mass Index (BMI) is a person's weight in kilograms (or pounds) divided by the square of height in meters (or feet). A high BMI can indicate high body fatness.")
        st.image("bmi.jpg")
    with st.expander("Plasma Glucose Concentration"):
        st.write("A plasma glucose test is a measure of how much sugar/glucose you have circulating in your blood. “Random” or “Casual” simply means that you have blood drawn at a laboratory at any time. Whether you have fasted or recently eaten will not affect the test.")
        st.image("bp1.jpg")
    with st.expander("Diastolic Blood Pressure"):
        st.write("Blood pressure is measured using two numbers: The first number, called systolic blood pressure, measures the pressure in your arteries when your heart beats. The second number, called diastolic blood pressure, measures the pressure in your arteries when your heart rests between beats.")
        st.image("bp.jpg")

        
   
    