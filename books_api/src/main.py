from fastapi import FastAPI

from src.author.views import router as author_view
from src.book.views import router as book_router

app = FastAPI()
app.include_router(author_view, prefix="/authors", tags=["authors"])
app.include_router(book_router, prefix="/books", tags=["books"])
