from fastapi import FastAPI
from routes import users,products

app=FastAPI(title="FASTAPI Modular Project")

# include routes

app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"message":"Welcome to Modular FASTAPI Project!!"}