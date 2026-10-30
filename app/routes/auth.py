from fastapi import APIRouter, HTTPException

from app.models.user import RegistrationData, LoginData
from app.errors.user_errors import UsernameAlreadyExistsError, InvalidCredentialsError
from app.services.user_service import create_user, authenticate_user
from app.services.session_services import user_has_active_session, create_session, delete_session


router_auth = APIRouter()

@router_auth.post("/auth/signup",status_code=201)
def signup(userdata : RegistrationData): 
    try : 
        create_user(userdata)
        return {"message":"Account created successfully"}
        
    except UsernameAlreadyExistsError: 
        raise HTTPException(status_code=409, detail="Username Already Exists")




@router_auth.post("/auth/signin",status_code=200)
def signin(userdata: LoginData): 


    # Verify username/password
    username = userdata.username
    password = userdata.password

    try : 
        user_id = authenticate_user(username,password)
    
    except InvalidCredentialsError: 
        raise HTTPException(status_code=401, detail="Invalid username or password")


    # Check whether this user already has an active session
    # If not, create a session and return its session_id
    if userdata.replace_session : 
        delete_session(user_id)
        session_id = create_session(user_id)

    else : 
        if not user_has_active_session(user_id): 
            session_id = create_session(user_id)
    
        # If yes, tell the frontend that another session is active
        else : 
            raise HTTPException( status_code=409,detail="An active session already exists")

    return {"session_id" : session_id}