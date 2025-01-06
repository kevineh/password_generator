"""
File: backend/app/main.py
Purpose: FastAPI application entry point and configuration
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import password
from app.database import engine, Base

app = FastAPI(title="Password Generator API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(password.router, prefix="/api", tags=["password"])
