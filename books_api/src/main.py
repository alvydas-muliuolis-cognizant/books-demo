from fastapi import FastAPI, status
from fastapi.exception_handlers import (
    http_exception_handler,
)
from fastapi.responses import JSONResponse
from src.author.views import router as author_view
from src.book.views import router as book_router
from starlette.exceptions import HTTPException
from starlette.requests import Request

from .logging import get_logger

logger = get_logger(__name__)

app = FastAPI()


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"SERVER ERROR: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred."},
    )


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP ERROR: {exc.detail}", exc_info=True)
    return await http_exception_handler(request, exc)


app.include_router(author_view, prefix="/authors", tags=["authors"])
app.include_router(book_router, prefix="/books", tags=["books"])
