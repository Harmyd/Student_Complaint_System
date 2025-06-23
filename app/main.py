from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return{"data":"Student Complaints System Api"}