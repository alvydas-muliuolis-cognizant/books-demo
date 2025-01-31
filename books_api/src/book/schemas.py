from pydantic import BaseModel, Field

from src.author.schemas import AuthorResponse
from src.publisher.schemas import PublisherResponse


class BookResponse(BaseModel):
    id: int
    title: str
    authors: list[AuthorResponse]
    overview: str
    isbn13: str
    pages: int
    publisher: PublisherResponse


class BookCreateRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    authors: list[int]
    overview: str = Field(min_length=10, max_length=1000)
    isbn13: str = Field(min_length=13, max_length=13, pattern=r"^[0-9]*$")
    pages: int = Field(gt=0)
    publisher: int
