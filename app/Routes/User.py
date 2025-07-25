from fastapi import Depends,status,APIRouter,UploadFile,File
from ..databases import Session,get_db
from ..Util.Oauth import get_token
from ..Services.User import upload_profile_image


User=APIRouter(
               prefix="/users",
               tags="Users"
               )
@User.post("/upload_profile_pic",status_code=status.HTTP_200_OK)
def Upload_picture(
    Picture:UploadFile=File(default=None),
    db:Session=Depends(get_db),
    user=Depends(get_token)
):
    return upload_profile_image.upload_profile_image(Picture,db,user)