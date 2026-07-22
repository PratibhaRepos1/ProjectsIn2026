from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    business_name: str
    business_slug: str
    industry: str = "other"
    full_name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: str
    email: str
    full_name: str
    role: str
    business_id: str

    class Config:
        from_attributes = True
