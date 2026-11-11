import streamlit as st 
from streamlit_repositories import create_repository

def show_dashboard(): 
   with st.sidebar:
        repositories = st.button("Repositories")
        new_repository = st.button("New repository")
   if new_repository: 
        st.session_state["page"] = "NewRepository"
        st.rerun()
   elif repositories: 
        st.session_state["page"] = "Repositories"
        st.rerun()
        
   if st.session_state["page"] == "NewRepository": 
        create_repository()