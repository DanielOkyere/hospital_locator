from api.database import Base
from sqlalchemy import Column, Integer, String, Float
from geoalchemy2 import Geometry


class Hospital(Base):
    """Model for Class"""

    __tablename__ = 'hospital'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    coordinates = Column(Geometry(geometry_type='POINT', srid=4326))
    longitude = Column(Float)
    latitude = Column(Float)
    specialisation = Column(String)
    address = Column(String)
