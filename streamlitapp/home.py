import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Vuelos",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

fing = Image.open('./images/ingenieria.png')
uach = Image.open('./images/uach.png')

col1, col2, col3 = st.columns(3)    
with col1:
    st.image(fing,width=100)
with col3:
    st.image(uach,width=100)

with col2:
    st.markdown("# Tracker de Vuelos 🛫")
    st.markdown("### Computo paralelo y distribuido")
    st.markdown("#### Juan Angel Cepeda Fernandez")
    st.markdown("#### Manuel Alfonso Balderrama Chaparro")
    st.markdown("#### Miguel Alan Quintana Montaño")

    st.markdown("_Nota: Las pestañas se encuentran en un sidebar._")
