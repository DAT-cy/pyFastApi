from fastapi import FastAPI, Depends
from starlette import schemas

from db import engine, Base

import service, dto.schema , entity.models
from db import get_db , engine
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)



@app.get("/student",response_model=list[dto.schema.Class])
def get_student(db: Session = Depends(get_db)):
    return service.get_student(db);
@app.post("/student",response_model=dto.schema.Class)
def create_student(student: dto.schema.ClassCreate  , db: Session = Depends(get_db)):
    return service.create_student(db, student)

