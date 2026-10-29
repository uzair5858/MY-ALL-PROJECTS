from pydantic import BaseModel, field_validator, model_validator, computed_field  # type: ignore


class user(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):

        if len(v) < 4:
            raise ValueError("username must be at least 4 character")
        return v


class signupdata(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, value):

        if value.password != value.confirm_password:
            raise ValueError("passwords do not match")
        return value


class product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    