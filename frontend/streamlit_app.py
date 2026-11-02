import streamlit as st 

from streamlit_auth import show_signup, show_signin 

default_state = {
    "page":"Home",
    "session_id":None,
    "session_active" : False
}

for param, default_val in default_state.items(): 
    if param not in st.session_state: 
        st.session_state[param]= default_val

st.header("MiniForge")
if st.session_state["page"] == "Home" : 
    sign_up = st.button(label="Create your account")
    log_in = st.button(label="Log in")

    if sign_up : 
        st.session_state["page"] = "SignUp"
        st.rerun()

    if log_in : 
        st.session_state["page"] = "SignIn"
        st.rerun()

if st.session_state["page"] == "SignUp" : 
    show_signup()

elif st.session_state["page"] == "SignIn" : 
    show_signin()



