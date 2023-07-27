import streamlit as st
from utils.LOAD import load_models,load_forms_responses


# CSS style to hide Streamlit's main menu and footer
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# Applying the CSS style to hide Streamlit's main menu and footer
st.markdown(hide_st_style, unsafe_allow_html=True)


face_detector,face_recognizer = load_models()


st.header("Database Downloader")
year = st.selectbox('Pick year', ['2025', '2024','2023','2026'])

if year == '2025':
    temp = st.empty()
    temp.button("Load",on_click=load_forms_responses,args=(face_detector, face_recognizer,temp))

else:
    st.warning("Comming soon")
