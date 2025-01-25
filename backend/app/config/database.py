from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from typing import Optional

class DatabaseConfig:
    client: Optional[AsyncIOMotorClient] = None
    database_name: str = os.getenv('DATABASE_NAME', 'login_feature_db')

db = DatabaseConfig()

async def connect_to_mongo():
    mongodb_url = os.getenv('MONGODB_URL', 'mongodb://mongodb:27017')
    
    db.client = AsyncIOMotorClient(
        mongodb_url,
        serverSelectionTimeoutMS=5000,
        server_api=ServerApi('1')
    )
    
    try:
        # Verify the connection
        await db.client.admin.command('ping')
        print(f"Successfully connected to MongoDB at {mongodb_url}")
        
        # Test database access
        database = db.client[db.database_name]
        await database.command('ping')
        print(f"Successfully connected to database: {db.database_name}")
        
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        db.client = None
        raise e

async def close_mongo_connection():
    if db.client is not None:
        db.client.close()
        print("MongoDB connection closed")