from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

# Fake DB

new_books = [
    {"id": 1, "title" : "Harry Potter", "available": True},
    {"id": 2, "title" : "Eragon", "available": False},
    {"id": 3, "title" : "The Hobbit", "available": True},
    {"id": 4, "title" : "The Storyteller", "available": True}
]

# Home Route
@app.get("/") #search in Claude
def home():
    return {"message":"RJ's Library API"}


# 1. Get All Books (with availability)
@app.get("/new_books")
def get_all_books():
    return new_books

# 2. Get Only Available Books
@app.get("/new_books/available")
def get_available_books():
    available = [book for book in new_books if book["available"] == True]
    return available

# 3. Check Availability of a Specific Book
@app.get("/new_books/{book_id}")
def get_book(book_id: int):
    for book in new_books:
        if book["id"] == book_id:
            return {"title": book["title"], "available": book["available"]}
    raise HTTPException(status_code=404, detail="Book not found")

# 4. Update Title of a Book (PATCH)
class UpdateBook(BaseModel):
    title: str

@app.patch("/new_books/{book_id}")
def update_book(book_id: int, updated: UpdateBook):
    for book in new_books:
        if book["id"] == book_id:
            book["title"] = updated.title
            return {"message": "Book updated", "book": book}
    raise HTTPException(status_code=404, detail="Book not found")

    
