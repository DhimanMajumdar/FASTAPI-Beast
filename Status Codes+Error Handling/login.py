from pydantic import BaseModel
from fastapi import HTTPException, status,FastAPI

app=FastAPI()

class Login(BaseModel):
    username:str
    password:str

@app.post('/login')
def login_user(data:Login):
    if data.username!='admin':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Username not found"
        )
    if data.password !="12345":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wroong credentials!!"
        )
    return {
        "message":"Login successful!1",
        "user":data.username
    }