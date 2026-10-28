from app.models.users import RegistrationData
from app.database.user_queries import user_exists, insert_user
from app.errors.users_erros import UsernameAlreadyExistsError

from argon2 import PasswordHasher

password_hasher = PasswordHasher()

def create_user(userdata : RegistrationData): 

    #check if username already exists 
    if user_exists(userdata.username):   #définie dans user_queries
        raise UsernameAlreadyExistsError
    username = userdata.username

    #hash password 
    password_hash = _hash_password(userdata.password)

    #insert username and hashpassword in miniforge.db and get user_id 
    user_id = insert_user(username,password_hash)   #définie dans user_queries 

  
    return user_id 



def _hash_password(password : str): 

    password_hash = password_hasher.hash(password)
    return password_hash
  
