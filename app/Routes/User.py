from fastapi import Depends,status,APIRouter,UploadFile,File,Form
from ..databases import Session,get_db
from ..Util.Oauth import get_token
from ..Services.User import upload_profile_image,get_user_details,edit_user
from ..schema import UserOut
from typing import Optional


USER=APIRouter(
               prefix="/users",
               tags=["Users"]
               )
@USER.post("/upload_profile_pic",status_code=status.HTTP_200_OK)
def Upload_picture(
    Picture:UploadFile=File(default=None),
    db:Session=Depends(get_db),
    user=Depends(get_token)
):
    return upload_profile_image.upload_profile_image(Picture,db,user)

@USER.get("/get_user_detail",status_code=status.HTTP_200_OK,response_model=UserOut)
def user_info(db:Session=Depends(get_db),user=Depends(get_token)):
    return get_user_details.get_user_detail(db,user)

@USER.post("/edit_user_detail",status_code=status.HTTP_200_OK)
def edit_user_detail(
    Full_name:Optional[str]=Form(None),
    Matric_No:Optional[str]=Form(None),
    Department:Optional[str]=Form(None),
    Level:Optional[str]=Form(None),
    Email:Optional[str]=Form(None),
    profile_image:Optional[UploadFile]=File(default=None),
    db:Session=Depends(get_db),
    user=Depends(get_token)
):
    return edit_user.edit_user(Full_name,Matric_No,Department,Level,Email,profile_image,db,user)