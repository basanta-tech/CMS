from sqlalchemy.orm import Session
from models import Institution
from schemas import InstitutionCreate, InstitutionUpdate


def create_institution(db: Session, institution: InstitutionCreate):
    new_institution = Institution(**institution.dict())
    db.add(new_institution)
    db.commit()
    db.refresh(new_institution)
    return new_institution


def get_institutions(db: Session):
    return db.query(Institution).all()


def get_institution_by_id(db: Session, institution_id: int):
    return db.query(Institution).filter(Institution.institution_id == institution_id).first()


def update_institution(db: Session, institution_id: int, institution: InstitutionUpdate):
    db_institution = get_institution_by_id(db, institution_id)
    if not db_institution:
        return None
    for key, value in institution.dict(exclude_unset=True).items():
        setattr(db_institution, key, value)
    db.commit()
    db.refresh(db_institution)
    return db_institution


def delete_institution(db: Session, institution_id: int):
    db_institution = get_institution_by_id(db, institution_id)
    if not db_institution:
        return None
    db.delete(db_institution)
    db.commit()
    return db_institution
