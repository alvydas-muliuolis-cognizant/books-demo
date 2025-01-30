from fastapi import FastAPI

app = FastAPI()


@app.get("/books")
def get_books():
    return [
        {"title": "Python Crash Course"},
        {"title": "Automate the Boring Stuff with Python"},
    ]
