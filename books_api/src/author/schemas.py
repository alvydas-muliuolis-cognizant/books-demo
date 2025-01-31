from pydantic import BaseModel, Field


class AuthorResponse(BaseModel):
    id: int
    full_name: str


class AuthorCreate(BaseModel):
    full_name: str = Field(min_length=3, max_length=100)
