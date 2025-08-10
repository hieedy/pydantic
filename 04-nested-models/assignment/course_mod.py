from pydantic import BaseModel, Field


class Lesson(BaseModel):
    id: int
    topics: list[str] 


class Module(BaseModel):
    id: int
    name: str
    lessons: list[Lesson]

class Course(BaseModel):
    id: int
    name: str
    description: str | None = None
    modules: list[Module]