from fastapi import APIRouter, HTTPException

from app.models.user import RegistrationData
from app.errors.user_errors import UsernameAlreadyExistsError
from app.services.user_service import create_user


router_auth = APIRouter()

@router_auth.post("/auth/signup",status_code=201)
def signup(userdata : RegistrationData): 
    try : 
        create_user(userdata)
        return {"message":"Account created successfully"}
        
    except UsernameAlreadyExistsError: 
        raise HTTPException(status_code=409, detail="Username Already Exists")

        