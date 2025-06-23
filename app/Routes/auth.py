from ..databases import get_db,Session
from fastapi import Depends,APIRouter,status
from ..schema import UserSignUp
from ..Services import signup

signup= APIRouter(prefix="/auth")

@signup.post("/signup",status_code=status.HTTP_201_CREATED)
def signup(request:UserSignUp,db:Session=get_db()):
    return signup.signup(request,db)

