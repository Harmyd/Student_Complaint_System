from ..databases import get_db,Session
from fastapi import Depends,APIRouter,status
from ..schema import UserSignUp,Login
from ..Services.signup import SignUp
from ..Services.login import login

Auth= APIRouter(prefix="/auth",tags=["auth"])

@Auth.post("/signup",status_code=status.HTTP_201_CREATED)
async def Signup(request:UserSignUp,db:Session=Depends(get_db)):
    return await SignUp(request,db)

@Auth.post("/login",status_code=status.HTTP_200_OK)
async def Login(request:Login,db:Session=Depends(get_db)):
    return await login(request,db)
