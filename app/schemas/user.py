from pydantic import BaseModel, Field

# Base schema for common fields
class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    fullname: str = Field(min_length=3, max_length=100)

# Schema used when creating a new user (requires password)
class UserCreate(UserBase):
    password: str = Field(min_length=8)

# Schema used for reading/returning user data (never includes password)
class UserRead(UserBase):
    id: int

    # Configuration class for Pydantic V2 to work with SQLAlchemy models
    model_config = {
        "from_attributes": True  # Allows Pydantic to read ORM attributes (like id)
    }