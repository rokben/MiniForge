from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


from app.models.user import RegistrationData
from app.database.user_queries import user_exists, insert_user, get_user
from app.errors.user_errors import UsernameAlreadyExistsError, InvalidCredentialsError


password_hasher = PasswordHasher()

def create_user(userdata : RegistrationData): 

    #check if username already exists 
    if user_exists(userdata.username):  
        raise UsernameAlreadyExistsError
    username = userdata.username

    #hash password 
    password_hash = _hash_password(userdata.password)

    #insert username and hashpassword in miniforge.db and get user_id 
    user_id = insert_user(username,password_hash) 

    return user_id 



def _hash_password(password : str):

    password_hash = password_hasher.hash(password)
    return password_hash


def authenticate_user(username : str, password: str): 
    user = get_user(username)

    if not user :
        raise InvalidCredentialsError

    user_id = user[0]
    password_hash = user[1] 
    
    #verify password is good one 

    try : 
        password_hasher.verify(password_hash, password)
        return user_id
    
    except VerifyMismatchError : 
        raise InvalidCredentialsError
 
        
        
