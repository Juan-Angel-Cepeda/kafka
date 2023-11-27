import streamlit as st
import consumer as cs

consumer = cs.Consumer('mi-topic')
message = consumer.consume()

st.title('Fligth Tracker with Kafka')
st.write(message)


#st.map(consumer.consume(),latitude="lat",longitude="lng",zoom=4)

