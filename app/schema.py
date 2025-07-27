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

class UserOut(BaseModel):
    Full_name:str
    Matric_No:str
    Department:str
    Level:str
    Email:str
    profile_image:str

    class Config:
        from_attributes=True

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
    file_path:Optional[List[str]]=None
    status:str
    created_at:datetime

    class Config:
        from_attributes=True



    
