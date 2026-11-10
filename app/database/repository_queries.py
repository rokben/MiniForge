from .database import get_connection
from contextlib import closing


def insert_repository(user_id : int, repo_name : str, repo_description : str | None): 
    with closing(get_connection()) as connection : 
        with connection : 
            cur = connection.execute (
                """
                INSERT INTO repositories(user_id,repo_name,repo_description)
                VALUES(?,?,?);
                """, 
                (user_id,repo_name,repo_description)
            )
    return cur.lastrowid


def delete_repository(repo_id : int): 
    with closing(get_connection()) as connection : 
        with connection : 
            connection.execute (
                """
                DELETE FROM repositories
                WHERE repo_id =?;
                """, 
                (repo_id,)
            )