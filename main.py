from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed origins(Frontend URL)
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, # allowed frontend
    allow_credentials=True,
    allow_methods=["*"], # All method (GET, POST, PUT, DELETE)
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "message": "CORS enable api"
    }