import pandas
import numpy
import streamlit as st

st.title("Streamlit quick example")
x = st.slider('x')
st.write(x, 'squared is', x * x)