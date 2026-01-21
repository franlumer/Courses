from fastapi import  FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import auth

app = FastAPI()

app.include_router(auth.router)

# Exposicion de recursos estaticos segun el path
# app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get("/")
async def root():
    return "funciona"

