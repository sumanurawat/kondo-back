from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.routers import conversations

app = FastAPI()

# Configure Loguru (in your `main.py` or a dedicated logging module)
logger.add(
    "app.log",  # Log file name
    rotation="500 MB",  # Rotate log files every 500 MB
    compression="zip",  # Compress rotated log files
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {module} | {message}",  # Customize log format
)

# Include routers for conversations and messages
app.include_router(conversations.router)

# Allow requests from your React frontend (replace with your frontend URL)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Kondo API"}
