from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Step - 1: Ensure uploads folder exist
UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Step - 2: Static file setup
# URL: HTTP://127.0.0.1:8080/files/<filename>
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

# Step - 3: Upload file api
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    filep_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(
            status_code=400,
            detail="File not selected"
        )

    with open(filep_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File uploaded successfully",
            "filename": filename,
            "file_url": f"http://127.0.0.1:8080/files/{filename}"
        }

# Step - 4: Get file url api
@app.get("/files/{filename}")
def get_file(filename: str):
    filep_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(filep_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {
        "file_url": f"http://127.0.0.1:8080/files/{filename}"
    }

@app.get("/")
def home():
    return {
        "message": "File uploaded api running"
    }