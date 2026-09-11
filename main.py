from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "name": "Sad",
        "age": 29,
        "password": "Abc123"    # Here in response added password but when hit this api then in response not comes password, because here using response model
    }