
from typing import List, Optional
from pydantic import BaseModel

class addressw(BaseModel):
    street: str
    city: str
    postal_code: str


class user(BaseModel):
    id: int
    name: str
    address: addressw


class comment(BaseModel):
    id: int
    content: str
    replies: Optional[List[comment]] = None


# Objects
address = addressw(
    street="123 something",
    city="Jaipur",
    postal_code="10001"
)

user_obj = user(
    id=1,
    name="Hitesh",
    address=address
)

comment_obj = comment(
    id=1,
    content="first comment",
    replies=[
        comment(id=2, content="reply1"),
        comment(id=3, content="reply2")
    ]
)
