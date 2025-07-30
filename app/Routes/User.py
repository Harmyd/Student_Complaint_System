from fastapi import Depends,status,APIRouter,UploadFile,File,Form
from ..databases import Session,get_db
from ..Util.Oauth import get_token
from ..Services.User import upload_profile_image,get_user_details
from ..Services.User.edit_user import edit_user
from ..Services.User.get_user_details import get_user_detail
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
async def user_info(db:Session=Depends(get_db),user=Depends(get_token)):
    return await get_user_detail(db,user)

@USER.post("/edit_user_detail",status_code=status.HTTP_200_OK)
async def edit_user_detail(
    request:UserOut,
    db:Session=Depends(get_db),
    user=Depends(get_token)
):
    return await edit_user(request,db,user)