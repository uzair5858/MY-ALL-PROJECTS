from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class usersingup(BaseModel):
    username: str
    email: EmailStr
    password: str  # fixed typo 'passward' -> 'password'

    class settings(BaseModel):
        app_name: str = "chai app"
        admin_email: str = "admin@chai.com"

# Dependency to get settings
def get_settings():
    return usersingup.settings()

@app.post("/signup")
def signup(user: usersingup):
    return {'message': f'user {user.username} signed up successfully'}

@app.get("/settings")
def get_settings_endpoints(settings: usersingup.settings = Depends(get_settings)):
    return settings