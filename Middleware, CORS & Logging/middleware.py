from fastapi import FastAPI, Request
app=FastAPI()

@app.middleware("http")
async def log_requests(request:Request,call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response=await call_next(response)
    print(f"Response status: {response.status_code}")
    return response


@app.get("/")
def home():
    return {"message":"Middleware test success!!"}