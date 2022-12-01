from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np

@st.cache(allow_output_mutation=True)
def load():
    return load_model('model.h5')
model = load()

st.write('# MNIST Recognizer')

