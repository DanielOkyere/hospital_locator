from api.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from geoalchemy2 import Geometry


class Hospital(Base):
    """Model for Class"""
    
    __tablename__ = 'hospital'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    coordinates=Column(Geometry(geometry_type='POINT', srid=4326))
    specialisation=Column(String)
    address=Column(String)