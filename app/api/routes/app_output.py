from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def app_output():
    return