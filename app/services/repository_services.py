import sqlite3

from app.database.repository_queries import insert_repository, delete_repository
from app.errors.exceptions import RepositoryAlreadyExistsError, RepositoryCreationError
from app.git_operations import create_bare_repository


def create_repository(user_id : int, repo_name : str , repo_description : str | None): 

    # Create the SQLite metadata 

    try :
        repo_id = insert_repository(user_id, repo_name, repo_description) 

    except sqlite3.IntegrityError :  
        raise RepositoryAlreadyExistsError

    # Create the Git bare repository

    try : 
        create_bare_repository(user_id, repo_name)

    except : 
        delete_repository(repo_id)
        raise RepositoryCreationError

    return repo_id



