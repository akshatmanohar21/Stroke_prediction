import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('depl.pkl', 'rb'))

st.title('Will the person get a stroke or not')

age= st.slider("age",10.00,50.00)
avg_glucose_level= st.slider("avg glucose level",5.00,500.00)
bmi= st.slider("bmi",1.00,100.00)



def predict():
    float_features = [float(x) for x in [age, avg_glucose_level, bmi]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)


    if(int(label)==1):
        st.success('The person will get a stroke ')
    else:
        st.success('The person will not get a stroke ')

trigger = st.button('Predict', on_click=predict)
