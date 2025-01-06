"""
File: backend/app/routes/password.py
Purpose: API endpoints for password generation and logging
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from app.database import get_db
from app.services.password_service import PasswordService
from app.models.password_log import PasswordLog

router = APIRouter()


@router.post("/generate")
async def generate_password(options: Dict, db: Session = Depends(get_db)):
    try:
        password = PasswordService.generate_password(
            length=options.get("length", 12),
            use_uppercase=options.get("useUppercase", True),
            use_symbols=options.get("useSymbols", True),
            use_numbers=options.get("useNumbers", True),
        )

        # Log the generation
        log = PasswordLog(
            length=options.get("length"),
            has_uppercase=str(options.get("useUppercase")),
            has_symbols=str(options.get("useSymbols")),
            has_numbers=str(options.get("useNumbers")),
        )
        db.add(log)
        db.commit()

        return {"password": password}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/log")
async def log_password_generation():
    # TODO: Implement timestamp logging
    pass
