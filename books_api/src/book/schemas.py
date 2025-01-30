from pydantic import BaseModel, Field


class AuthorResponse(BaseModel):
    full_name: str


class PublisherResponse(BaseModel):
    name: str


class BookResponse(BaseModel):
    id: int
    title: str
    authors: list[AuthorResponse]
    overview: str
    isbn13: str
    pages: int
    publisher: PublisherResponse


class BookCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
