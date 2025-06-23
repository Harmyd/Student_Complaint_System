from ..databases import Session
from ..models import Students
def signup(request,db:Session):
    
    new_students=Students(Full_name=request.Fullname,)

