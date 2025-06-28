from ..databases import Session
from ..models import Password_reset
from datetime import timedelta,datetime
from fastapi import status
from fastapi.responses import JSONResponse

def verify_code(request,db:Session):
    code=db.query(Password_reset).filter(Password_reset.Email==request.Email).first()
    if not code:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"reset code not found"}
        )
    Time_expired=code.Expires_at
    current_time=datetime.utcnow()
    if current_time>Time_expired:
        return JSONResponse(
            status_code=status.HTTP_410_GONE,
            content={"message":"code already expired"}
        )
    elif request.code != code.Code:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message":"code not match"}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message":"Code verified"}
        )