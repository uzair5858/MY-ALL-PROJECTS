from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# Input data
input_data = {'id': 101, 'name': "chaicode", 'is_active': True}

# Create User instance
user_instance = User(**input_data)

print(user_instance)
