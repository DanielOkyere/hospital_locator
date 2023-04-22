from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from api.models.user.schemas import UserSchema, Token, TokenData
from sqlalchemy.orm import Session
from api.depencies.db_depencies import get_db
from decouple import config
from datetime import timedelta
from api.models.user.crud import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
)

EXPIRY = config("EXPIRY_MINUTES")


router = APIRouter(
    prefix="/auth", tags=["auth"], responses={401: {"description": "Unauthorized"}}
)


@router.post("/token", response_model=Token,)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=float(EXPIRY))
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_active_user)]
):
    return current_user
