from fastapi import FastAPI
from sqlalchemy import select

from database import DbSession
from models import Book

app = FastAPI()


@app.get("/books")
async def get_books(db_session: DbSession):
    async with db_session as session:
        result = await session.execute(select(Book))
        return result.scalars().all()
