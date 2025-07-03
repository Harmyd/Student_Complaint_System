from .databases import Base
from sqlalchemy import ForeignKey,Column,Integer,String,DateTime
from sqlalchemy.orm import Relationship
from datetime import datetime

class Students(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    Full_name=Column(String)
    Matric_No=Column(String,unique=True,index=True)
    Department=Column(String)
    Level=Column(String,index=True)
    Email=Column(String,unique=True,index=True)
    Password = Column(String)
    
    complains=Relationship("Complains",back_populates="student")

class Complains(Base):
    __tablename__="complaints"
    id = Column(Integer,primary_key=True,index=True)
    name= Column(String)
    title = Column(String)
    student_id=Column(ForeignKey("students.id"))
    level=Column(String)
    description=Column(String,nullable=False)
    department=Column(String)
    file_path=Column(String,nullable=True)
    status= Column(String,default="Pending")
    created_at=Column(DateTime,default=datetime.utcnow)

    student=Relationship("Students",back_populates="complains")

class Password_reset(Base):
    __tablename__ = "reset_code"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True)
    code=Column(String,nullable=False)
    expires_at=Column(DateTime,nullable=False)