from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

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

class ComplaintOut(BaseModel):
    id:int
    name:str
    title:str
    matric_no:str
    level:str
    description:str
    department:str
    file_path:List[str]
    status:str
    created_at:datetime

    class Config:
        from_attributes=True



    
