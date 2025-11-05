from sqlalchemy import Column, Integer, String
from database import Base


class Institution(Base):
    __tablename__ = "CMS"

    institution_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    established_year = Column(Integer)
    address = Column(String(255))
    phone = Column(String(20))
    email = Column(String(100))
    website = Column(String(100))
    accreditation_status = Column(String(50))
    student_count = Column(Integer)
