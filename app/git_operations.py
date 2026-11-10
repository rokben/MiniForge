from pathlib import Path
from git import Repo 

def create_bare_repository(user_id : int, repo_name : str):
    project_root = Path(__file__).parent.parent
    path_repo = project_root / "repositories" / str(user_id) / f"{repo_name}.git" 
    Repo.init(path_repo, bare = True)
   