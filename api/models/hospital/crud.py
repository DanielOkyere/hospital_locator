from sqlalchemy.orm import Session
from .hospitals import Hospital
from typing import Annotated


def get_hospitals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Hospital).offset(skip).limit(limit).all()

def get_hospitalby_id(db: Session, hospital_id: int):
    return db.query(Hospital).filter(Hospital.id == hospital_id).first()

def get_hospitalby_name(db: Session, hospital_name: str):
    return db.query(Hospital).filter(Hospital.name == hospital_name).first()