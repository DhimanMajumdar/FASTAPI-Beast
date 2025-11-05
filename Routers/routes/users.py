from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router=APIRouter(prefix="/users",tags=["Users"])

class User(BaseModel):
    name:str
    age:int

users_db=[] 

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    users_db.append(user)
    return {
        "message":f"User {user.name} added successfully !!"
    }



@router.get("/")
def get_users():
    return {"total_users":len(users_db), "data":users_db}



@router.get("/{name}")
def get_user(name:str):
    for user in users_db:
        if user.name.lower()==name.lower():
            return user
    raise HTTPException(status_code=404, detail="User not found!!")

