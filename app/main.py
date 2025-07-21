from fastapi import FastAPI
from .databases import Base,engine
import os
from .Routes import auth,forgot_password,Complaint

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

Base.metadata.create_all(engine)
port=int(os.environ.get("PORT","8000"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def index():
    return{"data":"Student Complaints System Api"}

app.include_router(auth.Auth)
app.include_router(forgot_password.forgot_password)
app.include_router(Complaint.complaint)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=port)