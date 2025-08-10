from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def val_username(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')

        return v 
    

class SignUp(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError('Passwords do not match')
        return values
    
class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
    @computed_field
    def total_price_with_tax(self) -> float:
        tax_rate = 0.2
        return self.total_price * (1 + tax_rate)

prod = Product(name='Laptop', price=1000.0, quantity=2)
print(prod.total_price)  # Output: 2000.0
print(prod.total_price_with_tax)  # Output: 2400.0