import secrets
from datetime import datetime, timedelta

from app.database.session_queries import insert_session, session_exists, get_expires_at, delete_session, update_session

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

