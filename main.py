from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI()

# Create a rate limiter using the client's IP address
limiter = Limiter(key_func=get_remote_address)

# Connect the limiter to FastAPI
app.state.limiter = limiter

# Handle RateLimitExceeded exception
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)


@app.get("/hello")
@limiter.limit("5/minute")
def hello(request: Request):
    # This endpoint allows only 5 requests per minute per IP
    return {
        "message": "Hello from FastAPI"
    }