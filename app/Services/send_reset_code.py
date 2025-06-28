from ..databases import Session
from ..models import Students,Password_reset
from ..Util.validator import valid_email
from fastapi.responses import JSONResponse
from fastapi import status
from datetime import timedelta,datetime
from ..Util.code_generator import generate_code
from ..Util.email import send_email

def send_reset_code(request,db:Session):
    email_valid=valid_email(request.Email)
    if isinstance(email_valid,JSONResponse):
        return email_valid
    email=email_valid
    check_email=db.query(Students).filter(Students.Email==email).first()
    if not check_email:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message":"Email not found"}
        )
    
    Otp_code = generate_code(4)
    expiry=datetime.utcnow()+timedelta(minutes=1)
    
    reset_code=Password_reset(Email=check_email.Email,Code=Otp_code,Expires_at=expiry)
    db.add(reset_code)
    db.commit()
    db.refresh(reset_code)

    try:
        send_email(Otp_code,check_email.Email)
    except Exception as e:
        db.delete(reset_code)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            content={"message":f"failed to send email: {str(e)}",
                     "Time":expiry}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message":"Reset code is sent successfully",
                 "expiry_time":expiry}
    )





