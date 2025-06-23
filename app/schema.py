from pydantic import BaseModel
from typing import List

class UserSignUp:
    Fullname:str
    Matric_no:int
    Department:str
    Level:str
    Email:str
    Password:str


