from db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Student(Base):
    __tablename__ = "tbl_student"

    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    age = Column(String,nullable=False)
    category = Column(String, nullable=False)
    school = Column(String, nullable=False)


