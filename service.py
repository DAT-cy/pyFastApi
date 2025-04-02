from entity.models import Student
from sqlalchemy.orm import Session
from dto.schema import ClassCreate
def create_student(db: Session , data : ClassCreate):
    student = Student(**data.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
def get_student(db: Session):
    return db.query(Student)()

