import streamlit as st
import consumer as cs

st.title('Fligth Tracker with Kafka')


lat = "20.919937"
lon = "-99.11438"

fligth_info = {
    "flight_id": "AMX123",
    "airline": "Aeromexico",
    "origin": "MEX",
    "destination": "MTY",
    "latitude": "20.919937",
    "longitude": "-99.11438"
}

st.map(fligth_info,zoom=15)