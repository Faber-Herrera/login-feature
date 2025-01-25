from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..models.auth import Token, LoginCredentials
from ..models.user import UserCreate, User
from ..services.user_service import UserService
from ..utils.auth import verify_password, create_access_token
from ..utils.dependencies import get_current_user

router = APIRouter()

@router.post("/register", response_model=User)
async def register(user_data: UserCreate):
    user_service = UserService()
    existing_user = await user_service.get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    user = await user_service.create_user(user_data)
    return User.from_orm(user)

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_service = UserService()
    user = await user_service.get_user_by_email(form_data.username)
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token)

@router.get("/me", response_model=User)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/test-user")  # Add GET method
@router.post("/test-user")
async def create_test_user():
    user_service = UserService()
    try:
        test_user = UserCreate(
            email="test@example.com",
            password="password123",
            name="Test User"
        )
        existing_user = await user_service.get_user_by_email(test_user.email)
        if existing_user:
            return {"message": "Test user already exists", "email": test_user.email}
            
        user = await user_service.create_user(test_user)
        return {"message": "Test user created successfully", "email": user.email}
    except Exception as e:
        return {"error": f"Could not create test user: {str(e)}"}