from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake DB
new_books = [
    {"id": 1, "title": "Harry Potter", "available": True},
    {"id": 2, "title": "Eragon", "available": False},
    {"id": 3, "title": "The Hobbit", "available": True},
    {"id": 4, "title": "The Storyteller", "available": True}
]

# Home Route
@app.get("/")
def home():
    return {"message": "RJ's Library API"}

# 1. Get All Books
@app.get("/new_books")
def get_all_books():
    return new_books

# 2. Get Only Available Books
@app.get("/new_books/available")
def get_available_books():
    return [book for book in new_books if book["available"] == True]

# 3. Check Availability of a Specific Book
@app.get("/new_books/{id}")
def get_book(id: int):
    for book in new_books:
        if book["id"] == id:
            return book
    

# 4. Update Title of a Book (PATCH)
class UpdateBook(BaseModel):
    title: str

@app.patch("/new_books/{id}")
def update_book(id: int, updated: UpdateBook):
    for book in new_books:
        if book["id"] == id:
            book["title"] = updated.title
            return {"message": "Book updated", "book": book}
   