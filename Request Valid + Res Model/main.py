# Input Validation

from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

class Product(BaseModel):
    name:str=Field(...,min_length=3,max_length=50,description="Product name between 3-50 chars")
    price:float=Field(...,gt=0,description="Price must be greater than 0")
    quantity:int=Field(...,ge=1,le=100,description="Quantity between 1-100")

@app.post("/add-product")
def add_product(item:Product):
    total=item.price*item.quantity
    return {"product":item.name, "total_value":total}    

# output Validation

   # 🧪 Even if tu extra data return kare, response_model usko trim kar dega.
   # FastAPI ensures only allowed fields show up in API response.

# Input model
class UserInput(BaseModel):
    name: str
    age: int
    email: str

# Output model
class UserOutput(BaseModel):
    name: str
    message: str

@app.post("/register", response_model=UserOutput)
def register_user(data: UserInput):
    msg = f"Welcome {data.name}, your registration is successful!"
    return {"name": data.name, "message": msg}
