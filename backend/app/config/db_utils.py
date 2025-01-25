from .database import db

def get_database():
    return db.client[db.database_name]