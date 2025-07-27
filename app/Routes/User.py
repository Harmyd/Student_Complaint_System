from fastapi import Depends,status,APIRouter,UploadFile,File
from ..databases import Session,get_db
from ..Util.Oauth import get_token
from ..Services.User import upload_profile_image,get_user_details
from ..schema import UserOut


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