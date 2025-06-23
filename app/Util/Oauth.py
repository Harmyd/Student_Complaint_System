from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from fastapi.responses import JSONResponse
from .Config import SECRET_KEY,Algorithm
from jose import jwt,JWTError

oauth2scheme=OAuth2PasswordBearer()
def get_token(Token:str=Depends(oauth2scheme)):
    try:
        decoded_token=jwt.decode(Token,SECRET_KEY,algorithms=Algorithm)
        User_id=decoded_token.get("students_id")
        Matric_no=decoded_token.get("matric_no")
        if not User_id or not Matric_no:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid token payload"
            )
        return {"user_id":User_id,"matric_no":Matric_no}
    except JWTError as e :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired or invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )



