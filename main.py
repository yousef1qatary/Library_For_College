#yousef khaled mohamed
#SE1
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

server = FastAPI()
origins = [
    "*"  # This allows all origins. For production, you'd list specific domains.
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, PATCH, DELETE)
    allow_headers=["*"],  # Allows all headers
)
# In-memory database of books
books = {
  1:{
    "id": 1,
    "title":"The Great Gatsby",
    "Author":"F.Scott Fitzgerald",
    "available_copies": 6
  },

  2:{
    "id": 2,
    "title":"1984",
    "Author":"George Orwell",
    "available_copies": 4
  },

  3:{
    "id": 3,
    "title":"To Kill a Mockingbird",
    "Author":"Harper Lee",
    "available_copies": 5
  },

  4:{
    "id": 4,
    "title":"Pride and Prejudice",
    "Author":"Jane Austen",
    "available_copies": 3
  },
}

# Health Check Endpoint
@server.get("/")
def health():
    return {"health": "OK", "status":"success"}

# Get All Books
@server.get("/books")
def show_all_books():
    return {"books":books , "status":"success"}

# Get Book by ID
@server.get("/books/{id}")
def show_book(id: int):
 if id in books: 
    return books[id]
 else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class new_book(BaseModel):
    id:int
    title:str
    Author:str
    available_copies:int

# Add New Book
@server.post("/books/{id}")
def add_new_books (book_details: new_book):
    new_id = max(books.keys()) + 1
    book = book_details.model_dump()
    books[new_id] = book
    return {"book": books[new_id], "status":"added successfully!"}

# Update Book
@server.put("/books/{id}")
def update_book(id:int, book_details: new_book):
    if id in books:
        book = book_details.model_dump()
        books[id] = book
        return {"book": books[id], "status":"updated successfully!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
class new_updated_book(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    Author: Optional[str] = None
    available_copies: Optional[int] = None

# Edit Book Details
@server.patch("/books/{id}")
def edit_details(id:int, book_details: new_updated_book):
    if id in books:
        book = book_details.model_dump(exclude_unset=True)
        books[id].update(book)
        return {"book": books[id], "status":"details edited successfully!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
# Borrow Book
@server.patch("/books/{id}/borrow")
def borrow_book(id:int):
    if id in books:
        if books[id]["available_copies"] > 0:
            books[id]["available_copies"] -= 1
            return {"book": books[id], "status":"book borrowed successfully!"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No copies available to borrow")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    
# Return Book
@server.patch("/books/{id}/return")
def return_book(id:int):
    if id in books:
        books[id]["available_copies"] += 1
        return {"book": books[id], "status":"book returned successfully!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
# Delete Book
@server.delete("/books/{id}")
def delete_book(id:int):
    if id in books:
        deleted_book = books.pop(id)
        return {"book": deleted_book, "status":"book deleted successfully!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
# Delete All Books
@server.delete("/books")
def delete_all_books():
    books.clear()
    return {"books": books, "status":"all books deleted successfully!"}


