from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas

router = APIRouter(prefix="/institutions", tags=["Institutions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.InstitutionResponse, status_code=status.HTTP_201_CREATED)
def create_institution(institution: schemas.InstitutionCreate, db: Session = Depends(get_db)):
    return crud.create_institution(db, institution)


@router.get("/", response_model=list[schemas.InstitutionResponse])
def read_institutions(db: Session = Depends(get_db)):
    return crud.get_institutions(db)


@router.get("/{institution_id}", response_model=schemas.InstitutionResponse)
def read_institution(institution_id: int, db: Session = Depends(get_db)):
    db_institution = crud.get_institution_by_id(db, institution_id)
    if not db_institution:
        raise HTTPException(status_code=404, detail="Institution not found")
    return db_institution


@router.put("/{institution_id}", response_model=schemas.InstitutionResponse)
def update_institution(institution_id: int, institution: schemas.InstitutionUpdate, db: Session = Depends(get_db)):
    updated = crud.update_institution(db, institution_id, institution)
    if not updated:
        raise HTTPException(status_code=404, detail="Institution not found")
    return updated


@router.delete("/{institution_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_institution(institution_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_institution(db, institution_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Institution not found")
    return