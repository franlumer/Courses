from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from db_users import User, db_users

router = APIRouter(prefix = "/users",
                   tags = ["Users"],
                   responses = {404 : {"error":"No encontrado"}})

@router.get("")
async def get_descriptions():
    return db_users

@router.get("/{user_name}")
async def get_user_by_id(user_name : str):
    for db_user in db_users:
        if db_user.name == user_name:
            return db_user
        
    raise HTTPException(status_code = 404, detail = "Usuario no encontrado")
        
@router.post("", status_code= 201)
async def create_user_test(user : User):
    for db_user in db_users:
        if validate_user(db_user, user):
            return validate_user(db_user, user)
        
    db_users.append(user)
    return {"status" : "Usuario creado"}, user

@router.put("") # actualizacion
async def update_user(user : User):
    for db_user in db_users:
        if db_user.id == user.id:
            db_user = user
            return {"status" : "Usuario actualizado"}, user
    
    return {"status" : "Usuario no encontrado"}

@router.delete("")
async def user(user : User):
    found = False
    for saved_user in db_users:
        if saved_user.id == user.id:
            db_users.remove(saved_user)
            found = True
    if found:
        return {"status" : f"Usuario eliminado"}
    else:
        return {"status" : f"Usuario no encontrado: user_id = {user.id}"}


def search_user(user_name: str):
    user = next((user for user in db_users if user.name.lower() == user_name.lower()), None) # devuelve el User (objeto) o None
    return user

def validate_user(db_user : User, new_user : User):
    if db_user.id == new_user.id:
        return {"error" : "La ID del usuario ya existe"}
    elif db_user.name == new_user.name:
        return {"error" : "El nombre del usuario ya existe"}
    elif db_user.email == new_user.email:
        return {"error" : "El e-mail ya fue registrado"}
