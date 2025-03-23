from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from database import todo_collection


def some_function():
    from serializers.todo import todo_serializer, todos_serializer  # ✅ Import inside function
    return todo_serializer, todos_serializer


class TodoCrud:
    @staticmethod
    def create_todo(todo_data):
        todo_data = jsonable_encoder(todo_data)
        todo_document = todo_collection.insert_one(todo_data)
        todo = todo_collection.find_one({"_id": ObjectId(todo_document.inserted_id)})
        return todo_serializer(todo)

    @staticmethod
    def get_todos():
        todos = todo_collection.find()
        return todos_serializer(todos)

    @staticmethod
    def get_todo(todo_id):
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo) if todo else None

    @staticmethod
    def update_todo(todo_id, todo_data):
        todo_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": jsonable_encoder(todo_data)})
        updated_todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(updated_todo)

    @staticmethod
    def delete_todo(todo_id):
        todo_collection.delete_one({"_id": ObjectId(todo_id)})
        return {"message": "Todo deleted successfully"}

todo_crud = TodoCrud()
