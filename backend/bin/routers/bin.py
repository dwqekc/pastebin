from fastapi import APIRouter,HTTPException
from controllers.bin import binquery

router = APIRouter()

@router.get("/bin/{bin}")
async def get_bin(bin):
    try:
        return await binquery.get_bin(bin)
    except:
        raise HTTPException(status_code=404,detail="no such bin")