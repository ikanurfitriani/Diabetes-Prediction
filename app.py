# MIT License

# Copyright (c) 2024 Ika Nurfitriani

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import streamlit as st
import pandas as pd
import numpy as np
import pickle

model_path = 'diabetes_model.pkl'
scaler_path = 'scaler.pkl' 

with open(model_path, 'rb') as file:
    model = pickle.load(file)

with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

def user_input_features():
    pregnancies = st.number_input('Pregnancies', 0, 20, 1)
    glucose = st.number_input('Glucose', 0, 300, 100)
    blood_pressure = st.number_input('Blood Pressure', 0, 150, 70)
    skin_thickness = st.number_input('Skin Thickness', 0, 99, 20)
    insulin = st.number_input('Insulin', 0, 900, 79)
    bmi = st.number_input('BMI', 0.0, 70.0, 32.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', 0.0, 3.0, 0.5)
    age = st.number_input('Age', 21, 100, 33)
    
    data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree_function,
        'Age': age
    }
    features = pd.DataFrame(data, index=[0])
    return features

st.title('Diabetes Prediction')

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

if st.button('Predict'):
    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)  

    st.subheader('Prediction')
    diabetes = np.array(['Non-diabetic', 'Diabetic'])
    st.write(diabetes[prediction][0])

    try:
        prediction_proba = model.predict_proba(df_scaled)  
        st.subheader('Prediction Probability')
        st.write(prediction_proba)
    except AttributeError:
        st.subheader('Prediction Probability')
        st.write("Probability estimates are not available for this model.")