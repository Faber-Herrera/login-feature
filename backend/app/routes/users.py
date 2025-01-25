from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/test")
async def test_users():
    return {"message": "Users router working"}