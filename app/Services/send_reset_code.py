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
    #check if email exists
    existing = db.query(Password_reset).filter(Password_reset.email==request.Email).first()
    if existing:
        existing.code=Otp_code
        existing.expires_at=expiry
    else:
        reset_code=Password_reset(email=check_email.Email,code=Otp_code,expires_at=expiry)
        db.add(reset_code)
        
    db.commit()
    try:
        send_email(Otp_code,check_email.Email)
    except Exception as e:
        db.delete(reset_code)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            content={"message":f"failed to send email: {str(e)}"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message":"Reset code is sent successfully",
                 "expiry_time":expiry.isoformat()}
    )





