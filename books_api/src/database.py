from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://admin:root@localhost:5432/books_demo_db"

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True),
)


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_session)]
