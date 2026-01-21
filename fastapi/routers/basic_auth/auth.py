from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

from db_users import UserDB, User, users_db

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(prefix="/login",
                   tags=["/login"])

def search_user(username : str) -> UserDB | None:
    if username in users_db:
        return UserDB(**users_db[username])
        # retorna el UserDB si es que existe en users_db
        # sino retorna None

async def current_user(token : str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales invalidas", 
                            headers={"WWW-Authenticate" : "Bearer"})
    if user.disabled:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo", 
                            headers={"WWW-Authenticate" : "Bearer"})
    return User(**users_db[token])

@router.get("")
async def login_get():
    return "Login funcionando"

@router.post("")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    db_user = search_user(form.username)
    if not db_user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")
    
    if form.password != db_user.password:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Contrasena incorrecta")
    
    else: 
        return {"status" : "loged", "access_token" : db_user.username, "token_type" : "bearer"}

@router.get("/users/me")
async def get_user_me(user : User = Depends(current_user)):
    return user