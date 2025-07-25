from ..databases import get_db,Session
from fastapi import Depends,APIRouter,status
from ..schema import UserSignUp,Login
from ..Services import signup,login

Auth= APIRouter(prefix="/auth",tags=["auth"])

@Auth.post("/signup",status_code=status.HTTP_201_CREATED)
def Signup(request:UserSignUp,db:Session=Depends(get_db)):
    return signup.SignUp(request,db)

@Auth.post("/login",status_code=status.HTTP_200_OK)
def Login(request:Login,db:Session=Depends(get_db)):
    return login.login(request,db)
