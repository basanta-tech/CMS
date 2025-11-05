FastAPI CMS — Institution Management System: 
A simple Content Management System (CMS) built with FastAPI and PostgreSQL, allowing full CRUD (Create, Read, Update, Delete) operations for managing institution records.

🚀 Features:
  Built with FastAPI (high performance and modern Python web framework)
  PostgreSQL database integration via SQLAlchemy ORM
  Pydantic models for data validation
  Full CRUD API for institutions
  Includes a Home Route and interactive Swagger Docs (/docs)

Project Structure
  CMS By FastApi/
  │
  ├── main.py                # Entry point of the application
  ├── database.py            # Database connection setup
  ├── models.py              # SQLAlchemy ORM models
  ├── schemas.py             # Pydantic models for validation
  │
  ├── routers/
  │   └── institutions.py    # All CRUD API routes
  │
  └── myenv2/                # (Your virtual environment)



API Endpoints:
  GET	/	Home route
  POST	/institutions/	Create new institution
  GET	/institutions/	Get all institutions
  GET	/institutions/{id}	Get institution by ID
  PUT	/institutions/{id}	Update institution
  DELETE	/institutions/{id}	Delete institution

  
Institution Model Fields
  institution_id : Primary Key
  name	
  type	
  established_year
  address	
  phone	
  email
  website
  accreditation_status
  student_count

  
✅ Example JSON (POST request)
{
  "name": "Nist University",
  "type": "University",
  "established_year": 1996,
  "address": "Golanthara, Berhmapur",
  "phone": "+91 63706 90928",
  "email": "details@nist.edu",
  "website": "https://www.nist.berhmapur.com",
  "accreditation_status": "Accredited",
  "student_count": 1600
}


Used Tech:
  FastAPI — Web framework
  SQLAlchemy — ORM for PostgreSQL
  Pydantic — Data validation
  Uvicorn — ASGI server

Author,
  Basanta Kumar Mohanty
