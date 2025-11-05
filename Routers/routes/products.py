from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter(prefix="/products",tags=["Products"])

class Product(BaseModel):
    name:str
    price:float

products=[]

@router.post("/")
def add_product(item:Product):
    products.append(item)
    return {"message":f"{item.name} added successfully !!" , "total_products":len(products)}

@router.get("/")
def get_products():
    return products