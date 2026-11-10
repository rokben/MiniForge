import secrets
from datetime import datetime, timedelta

from app.database.session_queries import insert_session, session_exists, get_expires_at, delete_session, update_session, get_session
from app.errors.exceptions import InvalidSession, ExpiredSession

def create_session(user_id : int):
    session_id = secrets.token_hex(16)
    expires_at = datetime.now() + timedelta(minutes=15)

    #Insert the session into the miniforge database
    insert_session(session_id,user_id,expires_at)

    return session_id



def user_has_active_session(user_id: int): 
    if not session_exists(user_id): 
        return False

    expires_at = datetime.fromisoformat(get_expires_at(user_id))
    
    if expires_at > datetime.now(): 
        return True 
    
    delete_session(user_id)
    return False


def refresh_session(user_id:int): 
    expires_at = datetime.now() + timedelta(minutes=15)
    update_session(user_id,expires_at)

def validate_session(session_id : str) : 
    session = get_session(session_id)

    # Invalid session
    if not session :
       raise InvalidSession 


    user_id, expires_at = session 
    expires_at = datetime.fromisoformat(expires_at)

    #Expired session, user has to log in again 
    if expires_at <= datetime.now(): 
        delete_session(user_id) 
        raise ExpiredSession 
 
    refresh_session(user_id)
    return user_id 