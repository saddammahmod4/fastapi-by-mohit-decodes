from fastapi import FastAPI

app = FastAPI()

# Users Route
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


# Query Params
@app.get("/students")
def get_student(name: str = None):
    return {
        "student name": name
    }

# Handle multiple query params
@app.get("/items")
def get_items(name: str = None, price: int = 10):
    return {
        "Name": name,
        "Price": price
    }
