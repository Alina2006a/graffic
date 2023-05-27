import streamlit as st
from PIL import Image

st.title('Мой сайт')

st.write('Какой то текст')

color = st.radio(
    "выберите цвет",
    ('#F90001', '#03F67A', '#2CC912'))
if color == '#F90001' :
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#F90001')
    image = Image.open('red.jpg')
    st.write('The current color is', color)
    st.image(image, caption='Sunrise by the mountains')
elif color == '#03F67A':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#03F67A')
    image = Image.open('green.jpg')
    st.write('The current color is', color)
    st.image(image, caption='Sunrise by the mountains')
elif color == '#2CC912':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#2CC912')
    image = Image.open('linght green.jpg')
    st.write('The current color is', color)
    st.image(image, caption='Sunrise by the mountains')