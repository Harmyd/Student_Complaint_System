from ...databases import Session
from fastapi.responses import JSONResponse
from fastapi import status,UploadFile
from ...models  import Students
import cloudinary

async def edit_user(Full_name,Matric_No,Department,Level,Email,profile_image:UploadFile,db,user):
    userId=user["user_id"]
    if not userId:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Not authorised"}
        )
    #created a dictionary in so i can easily use setattr func to update the present attr of the object
    updated_data={}
    if Full_name is not None:
        updated_data["Full_name"]=Full_name
    if Matric_No is not None:
        updated_data["Matric_No"]=Matric_No
    if Department is not None:
        updated_data["Department"]=Department
    if Level is not None:
        updated_data["Level"]=Level
    if Email is not None:
        updated_data["Email"]=Email
    if profile_image is not None:
        try:
            uploaded_image=cloudinary.uploader.upload(
                profile_image.file,
                folder="User_img",
                resource_type="image"
            )
            url=uploaded_image["secure_url"]
            updated_data["profile_image"]=url
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"message":str(e)}
            )
    #fetching the students result from the database 
    user_record= db.query(Students).filter(Students.id==userId).first()
    if not user_record:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"User not found"}
        )
    for field,value in updated_data.items():    
        setattr(user_record,field,value)
    db.commit()
    db.refresh(user_record)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
                "message":"Updated",
                "Updated_data":updated_data
                }
    )


    




    

    