from ..databases import Session
from fastapi import status
from ..Util import validator,hash,Token
from fastapi.responses import JSONResponse 
from ..models import Students
from ..Util.hash import Hash

def login(request,db:Session):

    Email_valid=validator.valid_email(request.Email.strip().lower())
    if isinstance(Email_valid,JSONResponse):
        return Email_valid
    email=Email_valid
    
    Email_check=db.query(Students).filter(Students.Email==email).first()
    print(Email_check.Password)
    print(request.Password)
    
    if not Email_check:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"Email does not exist"}
        )
    Hasher=Hash()
    unhashed_Password=Hasher.verify_password(request.Password,Email_check.Password)
    print(unhashed_Password)
    if  unhashed_Password == False:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Wrong Password"}
        )
    else:
        token=Token.create_access_token(data={"students_id":Email_check.id,"matric_no":Email_check.Matric_No})
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                    "message":"Login successful",
                    "Token":token,
                    "Token_type":"Bearer"
                     }
        )
