from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from .Config import SECRET_KEY,Algorithm
from jose import jwt,JWTError

oauth2scheme=OAuth2PasswordBearer()
def get_token(Token:str=Depends(oauth2scheme)):
    decoded_token=jwt.decode(Token,SECRET_KEY,algorithms=Algorithm)
    


