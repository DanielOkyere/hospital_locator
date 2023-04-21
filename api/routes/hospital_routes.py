from fastapi import APIRouter, Depends, HTTPException
from api.models.hospital import schemas, crud
from api.depencies.db_depencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/hospitals", tags=["hospitals"], responses={"404": {"description": "Not Found"}}
)


@router.get("/", response_model=list[schemas.HospitalCreate])
def get_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hospitals = crud.get_hospitals(db, skip=skip, limit=limit)
    if hospitals is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospitals


@router.get("/{hospital_name}", response_model=list[schemas.HospitalCreate])
def get_hospitals_by_name(hospital_name: str, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    hospitals = crud.get_hospitalby_name(
        db, skip, limit, hospital_name=hospital_name)
    if hospitals is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospitals


@router.get("/id/{hospital_id}", response_model=schemas.HospitalCreate)
def get_hospitals_by_id(hospital_id: int, db: Session = Depends(get_db)):
    hospitals = crud.get_hospitalby_id(db, hospital_id=hospital_id)
    if hospitals is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospitals
