from fastapi import FastAPI

from book.views import router as book_router

app = FastAPI()


app.include_router(book_router, prefix="/books", tags=["books"])
