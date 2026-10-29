import streamlit as st 
import requests

BASE_URL = "http://127.0.0.1:8000"

st.header("MiniForge")
username = st.text_input(label="Username")
password = st.text_input(label="Password",type="password")
create_account = st.button(label="Create your account")

 
if create_account : 
    try : 
        response_create_account = requests.post(
            f"{BASE_URL}/auth/signup", 
            json= {
                "username" : username, 
                "password" : password

            }
        )
    except requests.exceptions.RequestException: 
        st.error("Unable to connect to MiniForge server")

    else : 
    
        if response_create_account.status_code == 422:
            for error_type, error_message in response_create_account.json().get("detail").items(): 
                st.error(f"{error_type} : {error_message}")

        elif response_create_account.status_code == 409 : 
            st.error("Username Already Exists")

        elif response_create_account.status_code == 201: 
            st.success("Account created successfully")

        else : 
            st.error("An unexpected error occurred")
