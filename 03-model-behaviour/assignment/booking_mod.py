from pydantic import BaseModel, Field
from pydantic import field_validator, model_validator, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., gt=0)
    price_per_night: float
    
    @computed_field
    def total_price(self) -> float:
        return self.nights * self.price_per_night
    