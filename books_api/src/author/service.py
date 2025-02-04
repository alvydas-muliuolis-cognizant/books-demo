from typing import Optional

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Author

from .schemas import AuthorCreate


async def get_all(db_session: AsyncSession, ids: Optional[list[int]] = None) -> Author:
    query = select(Author)
    if ids and len(ids):
        query = query.filter(Author.id.in_(ids))
    result = await db_session.execute(query)
    return result.scalars().all()


async def get(db_session: AsyncSession, author_id: int) -> Optional[Author]:
    query = select(Author).where(Author.id == author_id)
    result = await db_session.execute(query)
    return result.scalars().one_or_none()


async def create(db_session: AsyncSession, author_in: AuthorCreate) -> Author:
    author = Author(**author_in.model_dump())
    db_session.add(author)
    await db_session.commit()
    await db_session.refresh(author)
    return author


async def update_author(
    db_session: AsyncSession, author_id: int, author_in: AuthorCreate
) -> Author:
    query = (
        update(Author).where(Author.id == author_id).values(**author_in.model_dump())
    )
    await db_session.execute(query)
    await db_session.commit()
    return await get(db_session, author_id)


async def delete_author(db_session: AsyncSession, author_id: int):
    await db_session.execute(delete(Author).where(Author.id == author_id))
    await db_session.commit()
