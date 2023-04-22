from pydantic import BaseModel


class HospitalBase(BaseModel):
    id: int


class HospitalCreate(HospitalBase):
    name: str
    specialisation: str
    address: str
    longitude: float
    latitude: float

    class Config:
        orm_mode = True
