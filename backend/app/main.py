from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.database import connect_to_mongo, close_mongo_connection
from .routes import auth, users

app = FastAPI(title="Login Feature API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}