from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str
    
class User(UserBase):
    id: int | None
    is_active: bool | None
    email: str
    first_name: str
    last_name:str
    
    class Config:
        orm_mode = True

    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: str | None = None
    
class UserInDB(User):
    hashed_password: str