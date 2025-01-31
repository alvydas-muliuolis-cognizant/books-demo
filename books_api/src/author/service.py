from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Author


async def get_all(db_session: AsyncSession, ids: Optional[list[int]] = None) -> Author:
    query = select(Author)
    if ids and len(ids):
        query = query.filter(Author.id.in_(ids))
    result = await db_session.execute(query)
    return result.scalars().all()
