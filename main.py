"""
fastapi_cms/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── crud.py
├── routers/
│   └── institutions.py
├── requirements.txt
└── .env
"""
from fastapi import FastAPI
from database import Base, engine
from routers import institutions

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"welcome to the Content Management System"}


app.include_router(institutions.router)