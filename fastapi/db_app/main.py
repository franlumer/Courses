from fastapi import FastAPI, status
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm

from jose import jwt 
from passlib.context import CryptContext

from pydantic import BaseModel
from db.db_users import User, UserDB

app = FastAPI()
ALGORYTHM = 'HS256' # Firma y verificacion (TOKENS)
CRYPT = CryptContext(schemes=['argon2']) # Algoritmo de encritpacion (hashing) (CONTRASENAS)



@app.post('/users/me')
async def users():
    pass