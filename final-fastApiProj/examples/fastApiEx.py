from fastapi import FastApi, Depends 
from pydantic import BaseModel, EmailStr

app = FastApi()

class UserSignUp(BaseModel):
    usernaeme: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "FastAPI Example"
    admin_email: EmailStr = "sourah@gmail.com"
    support_email: EmailStr = "support@gmail.com"

# Dependency to provide settings
def get_settings():
    return Settings()


@app.post("/signup")
def signup(user: UserSignUp):
    return {
        "username": user.username,
        "email": user.email,
        "message": "User signed up successfully!"
    }

# Endpoint to get application settings
@app.get("/settings")
def get_app_settings(settings: Settings = Depends(get_settings)):
    return settings
