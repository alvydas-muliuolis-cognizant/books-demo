from fastapi import APIRouter

from src.database import DbSession

from .schemas import BookCreateRequest, BookResponse
from .service import (
    create,
    get_all,
)

router = APIRouter()


@router.get("", response_model=list[BookResponse])
async def get_books(db_session: DbSession):
    return await get_all(db_session)


@router.post("", response_model=BookResponse)
async def create_book(db_session: DbSession, book_in: BookCreateRequest):
    return await create(db_session, book_in)
