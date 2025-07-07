from ...databases import Session
from fastapi import UploadFile,File
from ...models import Complains,Students
from fastapi import status,HTTPException
import os
from fastapi.responses import JSONResponse
import cloudinary.uploader

def submit_Complaints(Name,Matric_no,Department,Level,Complaint_title,Description,File_path:UploadFile,db:Session,current_user):
    student_id=current_user["user_id"]
    student=db.query(Students).filter(Students.id==student_id).first()
    if not student:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"Student does not exist"}
        )
    try:
        url=None
        urls=[]
        if File_path:
            for File in File_path:
                result=cloudinary.uploader.upload(
                    File.file,
                    folder="Complaints_img",
                    resource_type="auto"
                )
                url = result["secure_url"]
                urls.append(url)
        
        complaint= Complains(name=Name,title=Complaint_title,matric_no=Matric_no,student_id=student.id,level=Level,description=Description,department=Department,file_path=urls)
        db.add(complaint)
        db.commit()
        db.refresh(complaint)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message":"Complaint submitted successfully"}

        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
