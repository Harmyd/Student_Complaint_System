from ..databases import Session
from ..models import Students
from ..Util import validator
from fastapi import status,HTTPException
from fastapi.responses import JSONResponse

def change_password(request,db:Session):
    password=validator.valid_password(request.Password)
    if isinstance(password,JSONResponse):
        return password
    new_password=password
    try:
        user=db.query(Students).filter(Students.Email==request.Email).first()
        if not user:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message":"User not found"}
            )
        user.Password=new_password
        db.add(user)
        db.commit()
        db.refresh(user)
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={"message":"password reset successfull"}
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))


    
    