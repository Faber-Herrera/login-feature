from bson import ObjectId
from ..models.user import UserCreate, UserInDB
from ..utils.auth import get_password_hash
from ..config.db_utils import get_database

class UserService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.users

    async def create_user(self, user: UserCreate) -> UserInDB:
        user_dict = user.dict()
        hashed_password = get_password_hash(user_dict["password"])
        user_in_db = UserInDB(
            **user_dict,
            hashed_password=hashed_password
        )
        await self.collection.insert_one(user_in_db.dict())
        return user_in_db

    async def get_user_by_email(self, email: str) -> UserInDB | None:
        user_dict = await self.collection.find_one({"email": email})
        if user_dict:
            return UserInDB(**user_dict)
        return None