from contextlib import closing
from datetime import datetime

from .database import get_connection


def insert_session(session_id : str,user_id : int ,expires_at : datetime):
    expires_at = expires_at.isoformat()
    with closing(get_connection()) as connection : 
        with connection : 
            connection.execute (
                """
                INSERT INTO sessions(session_id,user_id,expires_at)
                VALUES(?,?,?);
                """, 
                (session_id,user_id,expires_at)
            )

def session_exists(user_id : int ) -> bool: 
    with closing(get_connection()) as connection : 
            cur = connection.execute (
                """
                SELECT session_id
                FROM sessions
                WHERE user_id =?;
                """, 
                (user_id,)
            )
            return cur.fetchone() is not None 

def get_expires_at(user_id : int): 
    with closing(get_connection()) as connection : 
                cur = connection.execute (
                    """
                    SELECT expires_at
                    FROM sessions
                    WHERE user_id =?;
                    """, 
                    (user_id,)
                )
                return cur.fetchone()[0]

def update_session(user_id : int, expires_at: datetime):
    expires_at = expires_at.isoformat()
    with closing(get_connection()) as connection : 
        with connection : 
            connection.execute (
                """
                UPDATE sessions
                SET expires_at = ?
                WHERE user_id =?;
                """, 
                (expires_at,user_id,)
            )
    
def delete_session(user_id : int): 
    with closing(get_connection()) as connection : 
            with connection : 
                connection.execute (
                    """
                    DELETE FROM sessions
                    WHERE user_id =?;
                    """, 
                    (user_id,)
                )


      