from ..databases import Session
from ..models import Students
from fastapi.responses import JSONResponse
from fastapi import status,HTTPException
from ..Util import validator,Token,hash


def SignUp(request,db:Session):
    Email_valid=validator.valid_email(request.Email.strip().lower())
    Matric_number=request.Matric_no.strip().lower()

#return the error if email is not valid
    if isinstance(Email_valid,JSONResponse):
        return Email_valid
    email=Email_valid
    
    password_strength=validator.valid_password(request.Password)
    #return the error if password is not valid 
    if isinstance(password_strength,JSONResponse):
        return password_strength
    password=hash.Hash.hash_password(password_strength)
    
    #check if email and matric no already exist
    Email_check=db.query(Students).filter(Students.Email==Email_valid).first()
    Matric_no_check=db.query(Students).filter(Students.Matric_No==Matric_number).first()
    if Email_check :
        return JSONResponse(
            #status_code=status.HTTP_400_BAD_REQUEST,
            content={"message":"Email Exists"}
        )
    elif Matric_no_check:
        return JSONResponse(
            #status_code= status.HTTP_400_BAD_REQUEST,
            content={"message":"Matric_no Exists"}
        )
    else:
        try:
            new_students=Students(Full_name=request.Fullname,Matric_No=Matric_number,
                                Department=request.Department,Level=request.Level,Email=email,Password=password)
            db.add(new_students)
            db.commit()
            db.refresh(new_students)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                        "message":"Sign up Successfull",
                        "access_token":Token.create_access_token(data={"students_id":new_students.id,"matric_no":new_students.Matric_No}),
                        "Token_type":"Bearer"
                        }       
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
