from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int 
    name: str = Field(..., 
                      min_length=3,
                      max_length=50,
                      description='The name of the employee',
                      example='Sourabh Sharma'
                      )
    department: str | None = 'General'
    salary: float = Field(..., ge=10000)



empl = Employee(id=1, name='John Doe', salary=9999)
print(empl)