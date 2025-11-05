from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app=FastAPI()


origins=[
    "http://localhost:5173", # local server
    "https://yourfrontend.com" # deployed version
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # kis URL se request allow honi chahiye
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE sab allow
    allow_headers=["*"],  # saare headers allow
)

@app.get("/")
def read_root():
    return {"message": "CORS configured successfully!"}