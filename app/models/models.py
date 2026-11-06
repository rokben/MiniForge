from pydantic import BaseModel, Field


class RegistrationData(BaseModel) : 
    username : str = Field(min_length = 3, max_length = 30)
    password : str = Field(min_length = 12)



class LoginData(BaseModel) : 
    username : str 
    password : str 
    replace_session : bool = False


class RepositoryData(BaseModel):
    name : str = Field(min_length = 3, max_length = 100, pattern = r"^[a-zA-Z0-9_-]+$") 
    description : str | None = None 




