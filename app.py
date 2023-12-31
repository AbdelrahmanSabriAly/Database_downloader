import streamlit as st
from utils.LOAD import load_models,load_forms_responses
from PIL import Image


# CSS style to hide Streamlit's main menu and footer
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# Applying the CSS style to hide Streamlit's main menu and footer
st.markdown(hide_st_style, unsafe_allow_html=True)

# l,m,r = st.columns(3)
image = Image.open('g302-removebg-preview.png')

st.sidebar.image(image, caption='Reach The Futue')

face_detector,face_recognizer = load_models()


st.header("Database Downloader")
year = st.selectbox('Pick year', ['2025', '2024','2023','2026'])

if year == '2025':
    temp = st.empty()
    temp.button("Load",on_click=load_forms_responses,args=(face_detector, face_recognizer,temp,year))

else:
    st.warning("Comming soon")
