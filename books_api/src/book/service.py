from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.author import service as author_service
from src.models import Book
from src.publisher import service as publisher_service

from .schemas import BookCreateRequest


async def get_by_id(db_session: AsyncSession, id: int) -> Book:
    query = (
        select(Book)
        .options(joinedload(Book.authors))
        .options(joinedload(Book.publisher))
        .where(Book.id == id)
    )
    result = await db_session.execute(query)
    return result.scalars().first()


async def get_all(db_session: AsyncSession) -> list[Book]:
    query = (
        select(Book)
        .options(joinedload(Book.authors))
        .options(joinedload(Book.publisher))
    )
    result = await db_session.execute(query)
    return result.unique().scalars().all()


async def create(db_session: AsyncSession, book_in: BookCreateRequest) -> Book:
    authors = await author_service.get_all(db_session, book_in.authors)
    publisher = await publisher_service.get_by_id(db_session, book_in.publisher)
    book = Book(
        **book_in.model_dump(exclude={"authors", "publisher"}),
        authors=authors,
        publisher=publisher,
    )
    db_session.add(book)
    await db_session.flush()
    book_id = book.id
    await db_session.commit()
    return await get_by_id(db_session, book_id)
