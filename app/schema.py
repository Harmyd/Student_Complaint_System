from pydantic import BaseModel
from typing import List

class UserSignUp(BaseModel):
    Fullname:str
    Matric_no:int
    Department:str
    Level:str
    Email:str
    Password:str

class Login(BaseModel):
    Email:str
    Password:str

