from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from ..services.user_service import UserService
from ..utils.auth import verify_token
from ..models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = verify_token(token)
    if payload is None:
        raise credentials_exception
        
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
        
    user_service = UserService()
    user = await user_service.get_user_by_email(email)
    if user is None:
        raise credentials_exception
        
    return User.from_orm(user)