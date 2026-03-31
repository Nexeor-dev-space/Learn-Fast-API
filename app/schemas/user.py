from pydantic import BaseModel, Field, field_validator

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    fullname: str | None = Field(default=None, max_length=100)

    @field_validator("username", mode="before")
    @classmethod
    def normalize_username(cls, v: str) -> str:
        return v.strip()

    @field_validator("fullname", mode="before")
    @classmethod
    def normalize_fullname(cls, v: str | None) -> str | None:
        if v is None:
            return None
        return v.strip()

    @field_validator("username")
    @classmethod
    def username_not_empty(cls, v: str) -> str:
        if not v:
            raise ValueError("username cannot be empty")
        return v
    @field_validator("username")
    @classmethod
    def username_no_spaces(cls, v: str) -> str:
        if " " in v:
            raise ValueError("username must not contain spaces")
        return v


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=72)

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
