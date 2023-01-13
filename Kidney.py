# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 05:16:23 2023

@author: USER
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

kidney_model = pickle.load(open('model.pkl','rb'))


#For Background Image


page_bg_img = """

<style>

[data-testid="stAppViewContainer"]{
    background-image: url("https://i.ibb.co/DgSd2Z4/Pngtree-blue-medical-background-doctor-equipment-968595.jpg");
    background-size: cover;
    }


</style>

"""

st.markdown(page_bg_img, unsafe_allow_html=True)




# sidebar for navigate

with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           
                           ['Kidney Disease Prediction',
                            'Diabetes Prediction',
                            'Heart Disease Prediction'],
                           default_index = 0)
    
    
    
# Predicting Chronic Kidney page

if (selected == 'Kidney Disease Prediction'):
    
    # page title
    st.title('Kidney Disease Prediction using ML')
    
    
   # getting the input data from user
   
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
         Age = st.text_input('Age')
    
    with col2:
         Blood_Pressure = st.text_input('Blood Pressure')
    
    with col3:
         Specific_Gravity = st.text_input('Specific Gravity')
    
    with col4:
         Albumin = st.text_input('Albumin')
    
    with col1:
         Sugar = st.text_input('Sugar')
    
    with col2:
         Red_Blood_Cells = st.text_input('Red Blood Cells')
    
    with col3:
         Pus_Cell = st.text_input('Pus Cell')
    
    with col4:
         Pus_Cell_Clumps = st.text_input('Pus Cell Clumps')
    
    with col1:
         Bacteria = st.text_input('Bacteria')
    
    with col2:
         Blood_Glucose_Random = st.text_input('Blood Glucose Random')
    
    with col3:
         Blood_Urea = st.text_input('Blood Urea')
    
    with col4:
         Serum_Creatinine = st.text_input('Serum Creatinine')
    
    with col1:
         Sodium = st.text_input('Sodium')
    
    with col2:
         Potassium = st.text_input('Potassium')
    
    with col3:
         Hemoglobin = st.text_input('Hemoglobin')
    
    with col4:
         Packed_Cell_Volume = st.text_input('Packed Cell Volume')
    
    with col1:
         White_Blood_Cell_Count = st.text_input('White Blood Cell Count')
    
    with col2:
         Red_Blood_Cell_Count = st.text_input('Red Blood Cell Count')
    
    with col3:
         Hypertension = st.text_input('Hypertension')
    
    with col4:
         Diabetes_Mellitus = st.text_input('Diabetes Mellitus')
    
    with col1:
         Coronary_Artery_Disease = st.text_input('Coronary Artery Disease')
    
    with col2:
         Appetite = st.text_input('Appetite')
    
    with col3:
         Pedal_Edema = st.text_input('Pedal Edema')
    
    with col4:
         Anemia = st.text_input('Anemia')
    
    
    
    # code for Prediction
    kidney_diagnosis = ''
    kidney_prediction = ''
    
    
    
    # creating a button for Prediction
    
    if st.button('Diagnosis Result'):
       kidney_prediction = kidney_model.predict([[Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar, Red_Blood_Cells, Pus_Cell, Pus_Cell_Clumps, Bacteria, Blood_Glucose_Random, Blood_Urea, Serum_Creatinine, Sodium, Potassium, Hemoglobin, Packed_Cell_Volume, White_Blood_Cell_Count, Red_Blood_Cell_Count, Hypertension, Diabetes_Mellitus, Coronary_Artery_Disease, Appetite, Pedal_Edema, Anemia]])
        
    
   
    if (kidney_prediction == 0):
       kidney_diagnosis = 'Positive'
       
    if (kidney_prediction == 1):
         kidney_diagnosis = 'Negative'  
        
        
    st.success(kidney_diagnosis)
        
        
        
        
    
    
    
    
    
    
    
    