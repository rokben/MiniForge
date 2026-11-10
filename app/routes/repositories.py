from fastapi import APIRouter, Header, HTTPException

from app.models.models import RepositoryData
from app.services.session_services import validate_session
from app.services.repository_services import create_repository
from app.errors.exceptions import InvalidSession, ExpiredSession, RepositoryAlreadyExistsError, RepositoryCreationError

router_repositories = APIRouter()

@router_repositories.post("/repositories",status_code=201)
def create_repository_endpoint(repository_data : RepositoryData, session_id : str = Header(...)): 
    repo_name = repository_data.name
    repo_description = repository_data.description

    # Validate session and get user id 

    try : 
        user_id = validate_session(session_id)

    except InvalidSession : 
        raise HTTPException(status_code=401, detail="Invalid Session")


    except ExpiredSession : 
         raise HTTPException(status_code=401, detail="Expired Session")

    # Create repository 
    try : 
        repo_id = create_repository(user_id,repo_name,repo_description)

    except RepositoryAlreadyExistsError : 
        raise HTTPException(status_code=409, detail="Repository already exists")

    except RepositoryCreationError: 

        raise HTTPException(status_code=500, detail="Repository creation failed")

    return {"repo_id": repo_id, "message": "Repository created successfully"}
    
    
