import base64

import streamlit as st
from PIL import Image

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


add_bg_from_local('kotik.jpg')



st.title('Красочные цвета')

st.write('Красота красок в вашем предпочтении:)')

color = st.radio(
    "выберите цвет",
    ('красный', 'зелёный', 'светло-зелёный', 'голубой', 'синий', 'фиолетовый'))
if color == 'красный':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#F90001')
    st.write('The current color is', color)
    st.image(Image.open('red.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('red3.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('red4.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('red.2.jpg'), caption='Sunrise by the mountains')
elif color == 'зелёный':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#03F67A')
    st.write('The current color is', color)
    st.image(Image.open('green.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('green2.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('green3.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('green4.jpg'), caption='Sunrise by the mountains')
elif color == 'светло-зелёный':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#2CC912')
    st.write('The current color is', color)
    st.image(Image.open('linght green.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('linght green2.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('linght green3.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('linght green4.jpg'), caption='Sunrise by the mountains')
elif color == 'голубой':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#08CADC')
    st.write('The current color is', color)
    st.image(Image.open('light blue.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('light blue3.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('light blue2.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('light blue4.jpg'), caption='Sunrise by the mountains')
elif color == 'синий':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#0021F3')
    st.write('The current color is', color)
    st.image(Image.open('blue.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('blue2.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('blue3.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('blue4.jpg'), caption='Sunrise by the mountains')
elif color == 'фиолетовый':
    st.write('You selected comedy.')
    color2 = st.color_picker('Pick A Color', '#4D00F3')
    st.write('The current color is', color)
    st.image(Image.open('violet.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('violet2.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('violet3.jpg'), caption='Sunrise by the mountains')
    st.image(Image.open('violet4.jpg'), caption='Sunrise by the mountains')
