from fastapi import APIRouter

from database import DbSession

from .schemas import BookCreate, BookResponse
from .service import (
    create,
    get_all,
)

router = APIRouter()


@router.get("", response_model=list[BookResponse])
async def get_books(db_session: DbSession):
    return await get_all(db_session)


# TODO: fix this endpoint
@router.post("")
async def create_book(db_session: DbSession, book_in: BookCreate):
    return create(db_session, book_in)
