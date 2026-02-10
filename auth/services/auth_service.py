from sqlalchemy.orm import Session
from models.user import User
from core.security import hash_password, verify_password, create_token
from fastapi import HTTPException

def register_user(db: Session, email: str, password: str):

    existing = db.query(User).filter(User.email == email).first()

    if existing:
        raise HTTPException(400, "User exists")

    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()

    return {"status": "created"}


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(401, "Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"sub": user.email})

    return {"access_token": token}
