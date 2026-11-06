

class UsernameAlreadyExistsError(Exception): 
  pass 

class InvalidCredentialsError(Exception):
    pass

class InvalidSession (Exception): 
    pass 

class ExpiredSession(Exception): 
    pass 