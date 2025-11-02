from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app=FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello FastAPI 😊"}


@app.get("/hello/{name}")
def greet_user(name:str):
    return {"message":f"Hello {name}, welcome to FastAPI!"}

@app.post("/greet")
def greet_user(data:dict):
    name=data.get("name","Guest")
    return {"message":f"Hello {name}, nice to meet you"}

# by pydantic model
class UserInput(BaseModel):
    name:str
    age:int
    city:Optional[str]="Kanpur"

@app.post("/intro")
def intro(user:UserInput):
    return {
        "message":f"Hey {user.name}! You are {user.age} years old!!",
        "cool_level":"🔥"
    }   


# practice time

class sumInput(BaseModel):
    a:int
    b:int

@app.post("/sum")
def sum(data:sumInput):
    result=data.a+data.b
    return{"sum":result}

# path + query example

@app.get("/products/{category}")
def filter(category:str,limit:int=5, sort:str="asc"):
    return {
        "category": category,
        "limit": limit,
        "sort_order": sort,
        "message": f"Showing {limit} {category} products sorted {sort}",
    }

# practice time

class UserInp(BaseModel):
    unit:str
    val:float
# app.get("/convert/{unit}") -> yeh nhi chalega because we are using basemodel and usme body mein params pass nhi kar sakte in get call
@app.post("/convert/{unit}")
def convert(data:UserInp):
    if data.unit.lower() == "km":
        miles = data.val * 0.621371
        return {
            "unit": "km to miles",
            "input": f"{data.val} km",
            "output": f"{round(miles, 2)} miles"
        }

    elif data.unit.lower() == "c":
        fahrenheit = (data.val * 9/5) + 32
        return {
            "unit": "celsius to fahrenheit",
            "input": f"{data.val} °C",
            "output": f"{round(fahrenheit, 2)} °F"
        }

    else:
        return {"error": "Invalid unit! Use 'km' or 'c'."}
