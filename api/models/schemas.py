from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str

    
class UserSchema(UserBase):
    is_active: bool | None
    first_name: str | None
    last_name:str | None
    id: int
    
    class Config:
        orm_mode = True

    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: str | None = None
    
class UserInDB(UserSchema):
    hashed_password: str
    
class UserDelete(BaseModel):
    id: int | None = None