from fastapi import APIRouter
from controllers.paste import pastecommand

router = APIRouter()

@router.post("/paste/{data}")
async def paste(data):
    return await pastecommand.paste(data)