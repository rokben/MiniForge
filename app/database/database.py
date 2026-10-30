import sqlite3 
from pathlib import Path
from contextlib import closing

def get_connection(): 
    project_root = Path(__file__).parent.parent.parent
    data_dir = project_root / "data"
    data_dir.mkdir(exist_ok=True, parents=True)
    connection = sqlite3.connect(data_dir/"miniforge.db")
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection


def init_db(): 
    with closing(get_connection()) as connection : 
        with connection : 
            connection.execute (
            """
                CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password_hash TEXT
                    );
            """
            )
            connection.execute(
            """
                CREATE TABLE IF NOT EXISTS sessions(
                    session_id TEXT PRIMARY KEY, 
                    user_id INTEGER NOT NULL UNIQUE,
                    expires_at TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(user_id)

                    );
            """
            )
