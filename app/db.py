from pymongo import MongoClient
from app.config import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Collection for storing user data
users_collection = db.get_collection('users')
pages_collection = db.get_collection('pages')
posts_collection = db.get_collection('posts')
comments_collection = db.get_collection('comments')

# Helper function to get the collection from database
def get_collection(collection_name):
    return db[collection_name]