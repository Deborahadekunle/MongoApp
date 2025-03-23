from fastapi import FastAPI
from routers import user, todo

app = FastAPI()

app.include_router(user.router)
app.include_router(todo.router)

@app.get("/")
def home():
    return {"message": "Welcome to MongoDB TodoApp with FastAPI"}
