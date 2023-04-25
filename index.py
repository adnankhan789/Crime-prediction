import pickle
from pathlib import Path
import streamlit as st
import database as db
from PIL import Image
import streamlit_authenticator as stauth
st.set_page_config(page_title="Crime Prediction", page_icon=":bar_char", layout="wide")
users =db.fetch_all_users()
usernames = [user["key"]for user in users]
names = [user["name"]for user in users]
hashed_passwords = [user["password"]for user in users]
# the code mentioned above
hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")
name, authentication_status, username = authenticator.login("Login","main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)
if authentication_status:
    name, authentication_status, username = authenticator.login("Login", "main")
    st.markdown("<h1 style='text-align: center;'>Predicting Crime using Big data Analytics</h1>", unsafe_allow_html=True)
    st.sidebar.title(f"Welcome")

    st.markdown("""<style>.big-font {font-size:20px !important;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Crime prediction is a topic that has gained immense attention in recent years, as it has the potential to improve public safety and prevent crimes before they occur. With the help of advanced technology and machine learning algorithms, it is now possible to analyze large amounts of data and identify patterns that can be used to predict future criminal activities. A crime prediction website can serve as a valuable tool for law enforcement agencies and communities, providing them with real-time insights and alerts to help prevent crimes and keep people safe. By harnessing the power of data and technology, we can work towards a safer and more secure future for all.</p>', unsafe_allow_html=True)
    crime_daigram = Image.open('crime.jpg')
    st.image(crime_daigram, width = 1300)

        ###---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)


    authenticator.logout("Logout", "sidebar")
