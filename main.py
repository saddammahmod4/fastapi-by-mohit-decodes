from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# Dependency injection
def common_logic():
    return {
        "message": "Common logic executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data


# Reusable dependency injection
def get_current_user():
    return {
        "message": "sad"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user


# Depedency injection in real use case
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return {
        "user": "Authorized user"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {
        "message": "Secure data accessed",
        "User": user
    }