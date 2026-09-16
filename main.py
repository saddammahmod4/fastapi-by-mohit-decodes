from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Read environment variables
APP_NAME = os.getenv("APP_NAME")
APP_ENV = os.getenv("APP_ENV")
DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")

# Create FastAPI application
app = FastAPI(title=APP_NAME)


@app.get("/")
def home():
    return {
        "app_name": APP_NAME,
        "environment": APP_ENV,
        "debug": DEBUG
    }


@app.get("/config")
def config():
    return {
        "secret_key": SECRET_KEY
    }