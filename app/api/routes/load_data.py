from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def load_data():
    return