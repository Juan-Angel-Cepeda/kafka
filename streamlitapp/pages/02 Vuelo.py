import streamlit as st
import consumer as cs
from PIL import Image
import time

mx = Image.open('./images/bandera.png')

st.markdown('# Fight Tracker MX')
st.image('./images/bandera.png',width=100)
st.markdown('### Rastrea un número de vuelo MX')

if 'dataframe' not in st.session_state:
    st.session_state.dataframe = cs.got_data()

if 'selected_flight_data' not in st.session_state:
    st.session_state.selected_flight_data = None

if 'flight_numbers' not in st.session_state:
    st.session_state.flight_numbers = None

if 'selected_flight_number' not in st.session_state:
    st.session_state.selected_flight_number = None
    
st.markdown('Selecciona un numero de vueelo')
st.session_state.dataframe = cs.got_data()

st.session_state.flight_numbers = st.session_state.dataframe['flight_number'].unique()
st.session_state.selected_flight_number = st.selectbox('Numero de vuelo', st.session_state.flight_numbers)
go = st.button('Buscar')

if go:
    st.session_state.selected_flight_data = st.session_state.dataframe[st.session_state.dataframe['flight_number'] == st.session_state.selected_flight_number]
    st.write('Datos del vuelo seleccionado')
    st.write(st.session_state.selected_flight_data)
    st.map(st.session_state.selected_flight_data,latitude=st.session_state.selected_flight_data['lat'].mean(),longitude=st.session_state.selected_flight_data['lon'].mean(),zoom=3)

