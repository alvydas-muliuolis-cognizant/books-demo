from fastapi import FastAPI
from sqlalchemy import select

import models
import schemas
from database import DbSession

app = FastAPI()


@app.get("/books")
async def get_books(db_session: DbSession):
    async with db_session as session:
        result = await session.execute(select(models.Book))
        return result.scalars().all()


@app.post("/books")
async def create_book(db_session: DbSession, book_in: schemas.Book):
    book = models.Book(**book_in.model_dump())
    async with db_session as session:
        session.add(book)
        await session.commit()
