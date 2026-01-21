from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Description(BaseModel): # Description(id = id, user_id = user_id, description = "description", date = "date")
    id : int
    user_id : int
    description : str
    date : str

db_descriptions = [Description(id = 1, user_id = 1, description = "Luciano Merlo", date = "24/10"),
                   Description(id = 2, user_id = 2, description = "Florencia Blaz", date = "24/10")]

@router.get("/descriptions")
async def get_descriptions():
    return db_descriptions