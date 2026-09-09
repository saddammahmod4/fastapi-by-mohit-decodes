from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {
        "message": "Fastapi setup"
    }

@app.post("/create-user")
# def create_user(name: str, age: int):   # One way to handle single single
def create_user(user: User):   # Real world code
    return {
        "message": "User created successfully",
        "data": user
    }

