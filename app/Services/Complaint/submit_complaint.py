from ...databases import Session
from fastapi import UploadFile,File
from ...models import Complains,Students
from fastapi import status,HTTPException
import os
from fastapi.responses import JSONResponse
import cloudinary.uploader

def submit_Complaints(Name,Matric_no,Department,Level,Complaint_title,Description,File_path:UploadFile,db:Session):
    student=db.query(Students).filter(Students.Matric_No==Matric_no).first()
    if not student:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"Student does not exist"}
        )
    try:
        url=None
        if File_path:
            result=cloudinary.uploader.upload(
                File_path.file,
                folder="Complaints_img",
                resource_type="auto"
            )
            url = result["secure_url"]
        
        complaint= Complains(name=Name,title=Complaint_title,student_id=student.id,level=Level,description=Description,department=Department,file_path=url)
        db.add(complaint)
        db.commit()
        db.refresh(complaint)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message":"Complaint submitted successfully"}

        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
