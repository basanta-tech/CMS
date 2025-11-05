from pydantic import BaseModel, EmailStr
from typing import Optional


class InstitutionBase(BaseModel):
    name: str
    type: str
    established_year: Optional[int]
    address: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    website: Optional[str]
    accreditation_status: Optional[str]
    student_count: Optional[int]


class InstitutionCreate(InstitutionBase):
    pass


class InstitutionUpdate(InstitutionBase):
    pass


class InstitutionResponse(InstitutionBase):
    institution_id: int

    class Config:
        from_attributes = True