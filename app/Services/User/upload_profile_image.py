import cloudinary.uploader
from ...databases import Session
from fastapi import status,HTTPException,UploadFile
from fastapi.responses import JSONResponse
import cloudinary
from ...models import Students

def upload_profile_image(Picture:UploadFile,db:Session,user):
    userId=user["user_id"]
    if not userId:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Not authorised"}
        )
    try:
        result=cloudinary.uploader.upload(
            Picture.file,
            folder="User_img",
            resource_type="images"
        )
        url=result["secure_url"]
        #save in db
        user=db.query(Students).filter(Students.id==userId).first()
        if not user:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message":"User not found"}
            )
        user.profile_image=url
        db.commit()
        db.refresh(user)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message":"Profile picture uploaded successfully"}
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))


    
    


