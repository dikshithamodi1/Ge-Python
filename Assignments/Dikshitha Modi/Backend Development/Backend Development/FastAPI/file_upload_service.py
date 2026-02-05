from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from PIL import Image
import os
import time
from typing import Dict
import uuid

app = FastAPI()

# Directory to save uploaded files
UPLOAD_DIR = "static"
THUMB_DIR = os.path.join(UPLOAD_DIR, "thumbnails")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

# Dictionary to track processing status
processing_status: Dict[str, str] = {}

# Function to validate image type and size
def validate_image(file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG/PNG allowed.")
    
    file.file.seek(0, os.SEEK_END)
    size = file.file.tell()
    file.file.seek(0)
    if size > 2 * 1024 * 1024:  # 2 MB
        raise HTTPException(status_code=400, detail="File too large. Max size is 2MB.")

# Background task to generate thumbnail
def generate_thumbnail(file_path: str, thumb_path: str, task_id: str):
    # Simulate long processing
    time.sleep(5)
    
    # Optional actual thumbnail creation
    try:
        with Image.open(file_path) as img:
            img.thumbnail((128, 128))
            img.save(thumb_path)
        processing_status[task_id] = "completed"
    except Exception as e:
        processing_status[task_id] = f"failed: {str(e)}"

@app.post("/upload/image/")
async def upload_image(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    validate_image(file)
    
    # Generate unique filename
    file_ext = file.filename.split(".")[-1]
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.{file_ext}")
    
    # Save file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Track processing
    processing_status[file_id] = "processing"
    
    # Schedule background task
    thumb_path = os.path.join(THUMB_DIR, f"{file_id}_thumb.{file_ext}")
    background_tasks.add_task(generate_thumbnail, file_path, thumb_path, file_id)
    
    return JSONResponse({"message": "File received", "task_id": file_id})

@app.get("/upload/status/{task_id}")
def check_status(task_id: str):
    status = processing_status.get(task_id)
    if not status:
        raise HTTPException(status_code=404, detail="Task ID not found")
    return {"task_id": task_id, "status": status}
