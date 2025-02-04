from fastapi import APIRouter, HTTPException, status
from src.database import DbSession

from .schemas import AuthorCreate, AuthorResponse
from .service import (
    create,
    get,
    get_all,
)
from .service import (
    delete_author as delete,
)
from .service import (
    update_author as update,
)

router = APIRouter()


@router.get("", response_model=list[AuthorResponse])
async def get_authors(db_session: DbSession):
    return await get_all(db_session)


@router.get("/{author_id}", response_model=AuthorResponse)
async def get_autor(db_session: DbSession, author_id: int):
    author = await get(db_session, author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found",
        )
    return author


@router.post("", response_model=AuthorResponse)
async def create_author(db_session: DbSession, author_in: AuthorCreate):
    return await create(db_session, author_in)


@router.put("/{author_id}", response_model=AuthorResponse)
async def update_author(db_session: DbSession, author_id: int, author_in: AuthorCreate):
    return await update(db_session, author_id, author_in)


@router.delete("/{author_id}", response_model=None)
async def delete_author(db_session: DbSession, author_id: int):
    await delete(db_session, author_id)
