from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str
    
class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True