from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import UserCreate, UserLogin
from db.postgres import SessionLocal
from services.auth_service import register_user, login_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, data.email, data.password)


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, data.email, data.password)
