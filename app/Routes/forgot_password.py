from ..databases import get_db,Session
from ..schema import  ForgotPasswordRequest,VerifyCodeRequest,ResetPassword
from fastapi import Depends,status,APIRouter
from ..Services import send_reset_code,verify_reset_code,Reset_password

forgot_password=APIRouter(
    prefix="/forgot_password"
)

@forgot_password.post("/send_reset_code",status.HTTP_200_OK)
def reset_code(request:ForgotPasswordRequest,db:Session=Depends(get_db)):
    return send_reset_code.send_reset_code(request,db)

@forgot_password.post("/verify_code",status.HTTP_200_OK)
def verify_code(request:VerifyCodeRequest,db:Session=Depends(get_db)):
    return verify_reset_code.verify_code(request,db)

@forgot_password.post("/change_password",status.HTTP_201_CREATED)
def change_password(request:ResetPassword,db:Session=Depends(get_db)):
    return Reset_password.change_password(request,db)