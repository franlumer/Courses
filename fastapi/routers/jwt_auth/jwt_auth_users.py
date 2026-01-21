from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET_KEY = "e2cc25646cf4d8fcdea6de4657c00fe2f795e72e059b42c9390bb6c9514ee51b"

crypt = CryptContext(schemes=["argon2"])

class User(BaseModel): # User(id = id, name = "name", email = "email", age = age)
    username :str
    full_name : str
    email : str
    disabled : bool

class UserDB(User):
    password : str

users_db = {
    'luciano': {
        "username": "luciano",
        "full_name": "Luciano",
        "email": "franlumer09@gmail.com",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$KMW4d661dg7h/P9fa21N6Q$xXzHvesRRMBN5gbGlElJu93if4jx+YmBrPndLyU1W/c" # 123456
    },
    'florencia': {
        "username": "florencia",
        "full_name": "Florencia",
        "email": "bflorenciaaraceli@gmail.com",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$8773nlPqvbeWcs6ZU8r5fw$5X0wTR+ELmdB/7/IxLOfO9w8L/BQy0CC1eeg5Pk9PMk" # 654321
    },
    'franco': {
        "username": "franco",
        "full_name": "Franco",
        "email": "example.example@gmail.com",
        "disabled": True,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$KMW4d661dg7h/P9fa21N6Q$xXzHvesRRMBN5gbGlElJu93if4jx+YmBrPndLyU1W/c" # 123456
    }
}


def search_user(username : str) -> UserDB | None:
    if username in users_db:
        return UserDB(**users_db[username])
        # retorna el UserDB si es que existe en users_db
        # sino retorna None

@app.get("/")
async def root():
    return {"status" : "Funcionando"}

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    db_user = search_user(form.username)
    if not db_user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")
    
    if not crypt.verify(form.password, db_user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Contrasena incorrecta")
    
    expiration = datetime.utcnow() +  timedelta(minutes=ACCESS_TOKEN_DURATION)
    
    access_token = {"sub" : db_user.username, "exp" : expiration}

    return {"access_token" : jwt.encode(access_token, key = SECRET_KEY, algorithm=ALGORITHM), "status" : "loged", "token_type" : "bearer"}


async def auth_user(token : str = Depends(oauth2)):
    try:
        username = jwt.decode(token, key = SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username == None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas")
    
    db_user = search_user(username)
    if not db_user:  # Validar que el usuario existe
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")
    
    # Convertir UserDB a User (sin password)
    return User(**db_user.model_dump(exclude={"password"}))
    


async def current_user(user : User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo", 
                            headers={"WWW-Authenticate" : "Bearer"})
    return user


@app.get("/users/me")
async def me(user : User = Depends(current_user)):
    return user
