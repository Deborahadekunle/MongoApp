# serializers/user.py

def user_serializer(user):
    return {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}

def users_serializer(users):
    return [user_serializer(user) for user in users]
