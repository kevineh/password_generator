"""
File: backend/app/models/password_log.py
Purpose: SQLAlchemy model for password generation logs
"""

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func
from app.database import Base


class PasswordLog(Base):
    __tablename__ = "password_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    password = Column(String)
