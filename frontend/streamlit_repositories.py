import streamlit as st
import requests

from config import BASE_URL

def create_repository():
    repo_name = st.text_input("Repository name", 
                            placeholder = "my-project")
    
    repo_description = st.text_area("Description", 
                                    placeholder ="What is your project about ?", 
                                    help = "Optional")
    st.info("🔒 Private repository. Only you can access this repository in MiniForge V1.")
    create_repo = st.button("Create your repository",
                            type = "primary")
    
    if create_repo : 
        try :
            response_create_repository = requests.post(
                f"{BASE_URL}/repositories", 
                    json= {
                        "name" : repo_name, 
                        "description" : repo_description
                    }, 
                    headers={
                        "session-id" : st.session_state["session_id"]
                    }
            ) 
        except requests.exceptions.RequestException: 
                st.error("Unable to connect to MiniForge server")
        
        else : 
            
            if response_create_repository.status_code == 401 or response_create_repository.status_code == 422:
                detail = response_create_repository.json().get("detail")
                st.error(detail)

            elif response_create_repository.status_code == 409 : 
                st.error("Repository already exists")
            
            elif response_create_repository.status_code == 500 : 
                st.error("Repository creation failed")
                
            elif response_create_repository.status_code == 201: 
                st.success(response_create_repository.json()["message"])

            else : 
                st.error("An unexpected error occurred")