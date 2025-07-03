from fastapi import APIRouter,Depends,status,Form,UploadFile,File
from ..databases import Session,get_db
from ..Services.Complaint import submit_complaint
from typing import List


complaint=APIRouter(prefix="/complaint")
@complaint.post("/submit_complaint",status_code=status.HTTP_201_CREATED)
def submit_complaints(
    Name:str = Form(...),
    Matric_no:str = Form(...),
    Department:str = Form(...),
    Level:str = Form(...),
    Complaint_Title:str = Form(...),
    Description:str= Form(...),
    File_path:List[UploadFile]=File(...),
    db:Session=Depends(get_db)
):
    return submit_complaint(Name,Matric_no,Department,Level,Complaint_Title,Description,File_path,db)