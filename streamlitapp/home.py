import streamlit as st
import consumer as cs
import folium

st.title('Fight Tracker')
map_button = st.button('Map')

if map_button:
    dataframe = cs.got_data()
    st.map(dataframe,latitude=dataframe['lat'].mean(),longitude=dataframe['lon'].mean(),zoom=4)


"""
if map_button:
    consumer = cs.Consumer('mi-topic')
    for df in consumer.consume():
        mymap = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=4)
        for _, row in df.iterrows():
            folium.Marker([row['lat'], row['lon']], popup=row['flight']).add_to(mymap)

        map_placeholder.map(mymap)
"""