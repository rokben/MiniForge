from .database import get_connection
from contextlib import closing


def user_exists(username : str): 
     with closing(get_connection()) as connection : 
            cur = connection.execute (
            """
                SELECT username
                FROM users
                WHERE username =?;""", (username,)
            )
            return cur.fetchone() is not None 
                

    
def insert_user(username : str, password_hash:str): 
    with closing(get_connection()) as connection : 
        with connection : 
            cur = connection.execute (
                """
                INSERT INTO users(username,password_hash)
                VALUES(?,?);
                """, 
                (username,password_hash)
            )
    return cur.lastrowid


def get_user(username : str): 
    with closing(get_connection()) as connection : 
        cur = connection.execute (
        """
            SELECT user_id, password_hash
            FROM users
            WHERE username =?;""", (username,)
        )
        row = cur.fetchone()
    if not row: 
        return False
    return row[0], row[1]
    
    