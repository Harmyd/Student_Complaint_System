from ...databases import Session
from ...models import Complains,Students
from fastapi.responses import JSONResponse
from fastapi import status
from ...schema  import ComplaintOut
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
        content=jsonable_encoder({
                 "message":"Successfull",
                 "Complaints":[ComplaintOut.from_orm(c).dict() for c in complaint]
                 })
    )
  

def get_specific():
    pass


