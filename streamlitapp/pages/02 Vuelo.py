import streamlit as st
import consumer as cs
from PIL import Image
import time

mx = Image.open('./images/bandera.png')

st.markdown('# Fight Tracker MX')
st.image('./images/bandera.png',width=100)
st.markdown('### Rastrea un número de vuelo MX')

if 'dataframe2' not in st.session_state:
    st.session_state.dataframe2 = cs.got_data(2)

if 'selected_flight_data' not in st.session_state:
    st.session_state.selected_flight_data = None

if 'flight_numbers' not in st.session_state:
    st.session_state.flight_numbers = None

if 'selected_flight_number' not in st.session_state:
    st.session_state.selected_flight_number = None

if 'flag' not in st.session_state:
    st.session_state.flag = True
    
def refresh():
    st.session_state.dataframe2 = cs.got_data(2)
    info = st.session_state.dataframe2[st.session_state.dataframe2['flight_number'] == st.session_state.selected_flight_number]
    st.write(info)
    st.map(info,latitude=info['lat'].mean(),longitude=info['lon'].mean(),zoom=5)

st.markdown('Selecciona un numero de vueelo')
st.session_state.flight_numbers = st.session_state.dataframe2['flight_number'].unique()
st.session_state.selected_flight_number = st.selectbox('Numero de vuelo', st.session_state.flight_numbers)
go = st.button('Buscar')
otro_vuelo = st.button('Buscar otro vuelo',key='otro_vuelo') # Boton que busca otro vuelo

if go:
    st.session_state.selected_flight_data = st.session_state.dataframe2[st.session_state.dataframe2['flight_number'] == st.session_state.selected_flight_number] 
    st.write('Datos del vuelo seleccionado')
    st.write(st.session_state.selected_flight_data)
    # Mapa que nos indica con un punto rojo la ubicacion del avion a tiempo real
    st.map(st.session_state.selected_flight_data,latitude=st.session_state.selected_flight_data['lat'].mean(),longitude=st.session_state.selected_flight_data['lon'].mean(),zoom=4)
    
    # Actualiza la informacion de nuestro vuelo seleccionado
    while st.session_state.flag:
        st.session_state.selected_flight_data = cs.got_data(2)
        time.sleep(60)
        if otro_vuelo:
            st.session_state.flag = False
            st.session_state.dataframe2 = None
            st.session_state.selected_flight_data = None
            st.session_state.selected_flight_number = None
            st.session_state.flight_numbers = None
            break
        refresh()
        
        

    
    