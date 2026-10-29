from pydantic import BaseModel, Field, computed_field

class booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_nights: float

    @computed_field
    @property
    def total_amount(self) -> float:

        return self.nights * self.rate_per_nights
    