from fastapi import  FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login") # Indica que tipo de autenticacion es y donde se obtiene el token(/login)

class User(BaseModel):
    username : str
    full_name : str
    email : str
    disabled : bool

class UserDB(User):
    password : str

users_db = {
    'lumerlo' : {
        "username" : "lumerlo",
        "full_name" : "Luciano Merlo",
        "email" : "test@test.com",
        "disabled" : False,
        "password" : "123456"
    },
    'lumerlo2' : {
        "username" : "lumerlo2",
        "full_name" : "Luciano Merlo2",
        "email" : "test@test.com2",
        "disabled" : True,
        "password" : "654321"
    }
}

def search_user(username : str) -> UserDB | None:
    if username in users_db:
        return UserDB(**users_db[username])
    
async def curent_user(token : str = Depends(oauth2)):   # Depends indica que antes de ejecutar la funcion verifique oauth2
                                                        # oauth2 extrae el token del header y lo pasa como parametro "header"
                                                        # en caso de no haber token la funcion no se ejecuta
    user =  search_user(token)
    if not user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales invalidas", 
                            headers={"WWW-Authenticate" : "Bearer"})
    if user.disabled:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo", 
                            headers={"WWW-Authenticate" : "Bearer"})
    return user

    
@app.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user = search_user(form.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no encontrado")
    
    if not (form.password == user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contrasena incorrecta")
    
    return {"access token" : user.username, "token_type" : "bearer"}


@app.get("/users/me")
async def me(user : User = Depends(curent_user)):
    return user