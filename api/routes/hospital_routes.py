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
    print(hospitals)
    return hospitals
