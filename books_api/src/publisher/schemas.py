from pydantic import BaseModel


class PublisherResponse(BaseModel):
    id: int
    name: str
