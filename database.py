from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_DB_CONNECTION_URI"))
db = client["todoapp"]

user_collection = db["users"]
todo_collection = db["todos"]
