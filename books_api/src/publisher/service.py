from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Publisher


async def get_by_id(db_session: AsyncSession, id: int) -> Publisher:
    query = select(Publisher).where(Publisher.id == id)
    result = await db_session.execute(query)
    return result.scalars().first()
