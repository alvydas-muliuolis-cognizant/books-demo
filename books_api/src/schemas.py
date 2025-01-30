from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(min_length=3, max_length=100)
