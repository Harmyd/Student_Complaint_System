from pydantic import BaseModel
from typing import List,Optional

class UserSignUp(BaseModel):
    Fullname:str
    Matric_no:str
    Department:str
    Level:str
    Email:str
    Password:str

class Login(BaseModel):
    Email:str
    Password:str

class ForgotPasswordRequest(BaseModel):
    Email:str

class VerifyCodeRequest(BaseModel):
    Email:str
    Code:str

class ResetPassword(Login):
    pass



    
