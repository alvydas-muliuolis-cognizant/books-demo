from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from models import Book

from .schemas import BookCreate


async def get_all(db_session: AsyncSession) -> list[Book]:
    query = (
        select(Book)
        .options(joinedload(Book.authors))
        .options(joinedload(Book.publisher))
    )
    async with db_session as session:
        result = await session.execute(query)
        return result.unique().scalars().all()


async def create(db_session: AsyncSession, book_in: BookCreate) -> Book:
    book = Book(**book_in.model_dump())
    async with db_session as session:
        session.add(book)
        await session.commit()
    return book
