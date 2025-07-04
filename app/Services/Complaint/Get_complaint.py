from ...databases import Session
from ...models import Complains,Students
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

def get_user_complaint(db:Session,current_user):
    user_id=current_user['user_id']

    user=db.query(Students).filter(Students.id==user_id).first()
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"user not found"}
        )
    complaint=db.query(Complains).filter(Complains.student_id==user_id).all()
    if not complaint:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"No complaint found for this user"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message":"Successfull",
                 "Complaints":jsonable_encoder(complaint)}
    )
  

def get_specific():
    pass


