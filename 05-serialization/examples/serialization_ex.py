from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at : datetime 
    address: Address 
    tags: list[str] = [] 

    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.strftime('%d-%m-%YT%H:%M:%S')
        }
    )

if __name__ == "__main__":
    user = User(
        id = 1,
        name = 'Sourabh',
        email = 'sourabh@gmail.com',
        created_at = datetime(2024,3,15,14,30),

        address = Address(
            street = '123 Main St',
            city = 'Anytown',
            zip_code = '12345'
        ),
        tags = ['admin', 'user']
    )

    #model_dump -- used for serialization, expected to return a python dict
    user_data = user.model_dump()
    print(user_data)
    print(type(user_data))


    #model_dump_json -- used for serialization, expected to return a json string
    user_json_str = user.model_dump_json(indent=2)
    print(user_json_str)
    print(type(user_json_str))
