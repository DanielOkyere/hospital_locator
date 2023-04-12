from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from api.models.schemas import User, Token, TokenData
from jose import JWTError, jwt
from passlib.context import CryptContext
from decouple import config
from api.models.crud import get_user_by_email
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

SECRET_KEY = config('SECRET_KEYS')
ALGORITHM = config('ALGORITHM')
EXPIRY = config('EXPIRY_MINUTES')


router = APIRouter(
    prefix="/auth",
    tags=['auth'],
    responses={
        401: {"description": "Unauthorized"}
    }
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oaut2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    """Verify hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Generate hash for password"""
    return pwd_context.hash(password)

def authenticate_user(email: str, password: str):
    """Authenticate user using email and password"""
    user = get_user_by_email(Session, email)
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
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload: jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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

@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=EXPIRY)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/me/', response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user