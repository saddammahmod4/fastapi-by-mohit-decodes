from fastapi import FastAPI, Request
import time

app = FastAPI()

# Run this middleware for every HTTP request
@app.middleware("http")
async def my_middleware(request: Request, call_next):

    # Runs before the request reaches the API endpoint
    print("Request Received")

    # Send the request to the next middleware or API endpoint
    response = await call_next(request)

    # Runs after the API endpoint creates the response
    print("Response Sent")

    # Return the response back to the client
    return response




#### Log middleware
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(f"Path: {request.url.path} | Time: {process_time}")

    return response