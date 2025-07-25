from fastapi import APIRouter,Depends,status,Form,UploadFile,File
from ..databases import Session,get_db
from ..Services.Complaint import submit_complaint,Get_complaint
from typing import List,Optional
from ..schema import ComplaintOut
from ..Util.Oauth import get_token


complaint=APIRouter(prefix="/complaint",tags=["Complaint"])
@complaint.post("/submit_complaint",status_code=status.HTTP_201_CREATED)
def submit_complaints(
    Name:str = Form(...),
    Matric_no:str = Form(...),
    Department:str = Form(...),
    Level:str = Form(...),
    Complaint_Title:str = Form(...),
    Description:str= Form(...),
    File_path: Optional[List[UploadFile]]=File(default=None),
    db:Session=Depends(get_db),
    current_user=Depends(get_token)
):
    return submit_complaint.submit_Complaints(Name,Matric_no,Department,Level,Complaint_Title,Description,File_path,db,current_user)


@complaint.get("/get_complaints",status_code=status.HTTP_200_OK)
def get_complaint(db:Session=Depends(get_db),current_user=Depends(get_token)):
    return Get_complaint.get_user_complaint(db,current_user)