import streamlit as st
import requests


BASE_URL = "http://127.0.0.1:8000"

def show_signup(): 
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
                st.session_state["page"] = "SignIn"
                st.rerun()

            else : 
                st.error("An unexpected error occurred")

def show_signin(): 
    username = st.text_input(label="Username")
    password = st.text_input(label="Password",type="password")
    log_in = st.button(label="Log in")

    if log_in : 
        try : 
            response_log_in = requests.post(
                f"{BASE_URL}/auth/signin", 
                json= {
                    "username" : username, 
                    "password" : password, 

                }
            )
            
        except requests.exceptions.RequestException: 
            st.error("Unable to connect to MiniForge server")

        else : 
            if response_log_in.status_code == 422:
                for error_type, error_message in response_log_in.json().get("detail").items(): 
                    st.error(f"{error_type} : {error_message}")

            elif response_log_in.status_code == 401 : 
                st.error("Invalid username or password")

            elif response_log_in.status_code == 409: 
                st.error("An active session already exists. Replace it !")
                st.session_state["session_active"] = True
                
            elif response_log_in.status_code == 200: 
                st.success("Connected successfully")
                st.session_state["session_id"] = response_log_in.json()["session_id"]

            else : 
                st.error("An unexpected error occurred")

    if st.session_state["session_active"]: 
        replace_session = st.button(label="Replace session")
        if replace_session : 
            try : 
                response_log_in = requests.post(
                            f"{BASE_URL}/auth/signin", 
                            json= {
                                "username" : username, 
                                "password" : password, 
                                "replace_session" : True
            
                            }
                        )
            except  requests.exceptions.RequestException: 
                st.error("Unable to connect to MiniForge server")

            else : 
                if response_log_in.status_code == 422:
                    for error_type, error_message in response_log_in.json().get("detail").items(): 
                        st.error(f"{error_type} : {error_message}")
    
                elif response_log_in.status_code == 200: 
                    st.success("Connected successfully")
                    st.session_state["session_id"] = response_log_in.json()["session_id"]
                    st.session_state["session_active"] = False
    
                else : 
                    st.error("An unexpected error occurred")
            
            
       
        
    


