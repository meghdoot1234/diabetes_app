import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from PIL import Image

image = Image.open('logo.jpg')

st.image(image, caption='')

pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

#st.sidebar.header('Diabetes Prediction for females above 21 years')
#select = st.sidebar.selectbox('Select Form', ['Unhide to proceed'], key='1')
#if not st.sidebar.checkbox("Hide", True, key='2'):
st.title('Diabetes Prediction(Only for females above 21years of age)')
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
            st.write('Congratulation','You are not diabetic')
            st.caption(":red[_NB: The dataset used for this study is PIMA Indian Diabetes Dataset from Kaggle_]")
        else:
            st.write(" We are really sorry to say but it seems like you are Diabetic.")
            st.caption(":red[_NB: The dataset used for this study is PIMA Indian Diabetes Dataset from Kaggle_]")