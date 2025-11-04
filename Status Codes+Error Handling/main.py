# By default, FastAPI har route ke liye 200 OK deta hai.


# setting the headers

from fastapi import FastAPI, status
from fastapi import HTTPException
app=FastAPI()

@app.get('/ok',status_code=status.HTTP_200_OK)
def ok_response():
    return {"message":"Everything's fine bro 🔥"}

@app.post('/created',status_code=status.HTTP_201_CREATED)
def created_response():
    return {"message":"New resource created successfully!!"}

# Throwing exceptions + error handling


users={"dhiman":"pro","debojeet":"noob"}

@app.get('/user/{username}')
def get_username(username:str):
    if username  not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User '{username} not found"
        )
    return {"username":username,"level":users[username]}