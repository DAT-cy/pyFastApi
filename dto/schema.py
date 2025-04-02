from pydantic import BaseModel


class Class(BaseModel):
    name: str
    age: str
    category: str
    school: str


class ClassCreate(Class):
    pass


class ClassUpdate(Class):
    id: int

    class Config:
        from_attributes = True
