from pydantic import BaseModel

class HospitalBase(BaseModel):
    id: int

class HospitalCreate(HospitalBase):
    name: str
    specialisation: str
    address: str

    
    class Config:
        orm_mode = True
        
        
class HospitalOutputSchema(HospitalBase):
    name: str
    coordinates: dict
    specialisation: str
    address: str