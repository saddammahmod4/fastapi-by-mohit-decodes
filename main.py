from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

###### Simple way to handle exception ########
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     return {
#         "id": 1,
#         "name": "Sad"
#     }

class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

# This tells FastAPI: Whenever UserNotFoundException occurs, call user_not_found_handler.
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name: str):
    if name != "sad":
        raise UserNotFoundException(name)

    return {
        "name": name
    }
