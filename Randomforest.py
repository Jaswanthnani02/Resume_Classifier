import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from PIL import Image
 
model = joblib.load('rf_clf.pkl')

def web_app():

    st.write("""
    # Resume Classifier with Machine Learning
    ## This app predicts to which category a RTesume  belongs too
   """)
#     image = Image.open('customer_pic.png')

#     st.image(caption='Customer Behaviour Analysis')
    st.header("User Details")
    st.subheader("Kindly Enter The following Details in order to make a prediction")
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
    # Do something with the uploaded file
        st.write("You uploaded:", uploaded_file.name)
    
    


    
    if st.button("Press here to make Prediction"):
        
        result = model.predict(uploaded_file)
        if result == 0:
            result = "React JS Developer Resume"
        elif result == 1: 
            result = "PeopleSoft Resumes"
        elif result == 2: 
            result = "SQL Developer Lightning Insight Resumes"
        else :
            result = "Workday Resumes"
        
        st.text_area(label='Category belongs to:- ',value=result , height= 100)
    
run = web_app()
