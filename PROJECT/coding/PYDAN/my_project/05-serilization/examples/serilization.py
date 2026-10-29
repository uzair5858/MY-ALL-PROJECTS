
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class address(BaseModel):
    street: str
    city: str
    zip_code: str


class user(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: address
    tags: List[str] = []
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%y %H:%M:%S')}
    )


# create a user instance
user_obj = user(
    id=1,
    name="hitesh",
    email="hitesh@hc.com",
    created_at=datetime(2024, 3, 15, 14, 30),
    address=address(
        street="something",
        city="jaipur",
        zip_code="001144"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)


# model_dump() -> dict
python_dict = user_obj.model_dump()
print(python_dict)
print("===============================\n")

# using model_dump_json()
json_str = user_obj.model_dump_json()
print(json_str)