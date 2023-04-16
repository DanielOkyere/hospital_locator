from sqlalchemy.orm import Session
from .users import User
from .schemas import UserCreate
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from api.models.schemas import UserSchema, TokenData, UserInDB
from fastapi import status, HTTPException, Depends
from typing import Annotated
from decouple import config
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


SECRET_KEY = config("SECRET_KEYS")
ALGORITHM = config("ALGORITHM")
EXPIRY = config("EXPIRY_MINUTES")

oaut2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_SUserSchema(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_db_user(db):
    return UserInDB(**db)


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def verify_password(plain_password, hashed_password):
    """Verify hashed password"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Generate hash for password"""
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str):
    """Authenticate user using email and password"""
    user = get_user_by_email(db, email=email)
    # user = get_db_user(db=db_user)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=EXPIRY)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oaut2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def create_user(db: Session, user: UserCreate):
    hash_pass = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hash_pass,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int ):
    if isinstance(id, int):
        user = db.query(User).filter_by(id=id).first()
        db.delete(user)
        db.commit()
        return user