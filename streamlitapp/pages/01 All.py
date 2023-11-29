import streamlit as st
import consumer as cs
from PIL import Image
import time

mx = Image.open('./images/bandera.png')

st.markdown('# Fight Tracker MX')
st.image('./images/bandera.png',width=100)
st.markdown('### Muestra todas las aeronaves MX activas en tiempo real')

if 'dataframe' not in st.session_state:
    st.session_state.dataframe = cs.got_data(1)

st.session_state.dataframe = cs.got_data(1)
st.map(st.session_state.dataframe,latitude=st.session_state.dataframe['lat'].mean(),longitude=st.session_state.dataframe['lon'].mean())
st.dataframe(st.session_state.dataframe)

while True:
    time.sleep(60)
    st.rerun()
    
        


