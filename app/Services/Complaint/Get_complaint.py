from ...databases import Session
from ...models import Complains,Students
from fastapi.responses import JSONResponse
from fastapi import status

def get_user_complaint(db:Session,current_user):
    user_id=current_user['user_id']

    user=db.query(Students).filter(Students.id==user_id)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"user not found"}
        )
    Complaint=db.query(Complains).filter(Complains.student_id==user_id).all()
  
    pass

def get_specific():
    pass


