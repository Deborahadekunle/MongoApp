from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from database import user_collection
from serializers.user import user_serializer, users_serializer

class UserCrud:
    @staticmethod
    def create_user(user_data):
        user_data = jsonable_encoder(user_data)
        user_document = user_collection.insert_one(user_data)
        user = user_collection.find_one({"_id": ObjectId(user_document.inserted_id)})
        return user_serializer(user)

    @staticmethod
    def get_users():
        users = user_collection.find()
        return users_serializer(users)

    @staticmethod
    def get_user(user_id):
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user) if user else None

    @staticmethod
    def update_user(user_id, user_data):
        user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": jsonable_encoder(user_data)})
        updated_user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(updated_user)

    @staticmethod
    def delete_user(user_id):
        user_collection.delete_one({"_id": ObjectId(user_id)})
        return {"message": "User deleted successfully"}

user_crud = UserCrud()
