📚 FastAPI Library Manager

A full-stack web application for managing a simple library catalog. It consists of:

Backend: FastAPI using Python

Frontend: A single-page HTML/CSS/JavaScript app

Data Storage: In-memory Python dictionary

The project demonstrates basic CRUD operations: Create, Read, Update, and Delete, along with specific library actions like borrowing and returning.

Table of Contents

Features

Frontend Features

Backend Features

Project Structure

Getting Started

Prerequisites

1. Run the Backend (API Server)

2. Run the Frontend (Webpage)

API Documentation

Data Models

Endpoints

Examples (cURL)

Future Improvements

✨ Features

✨ Frontend Features (library_manager.html)

The user interface provides a complete management dashboard:

View All Books: Fetches and displays all books on page load.

Add New Book: A modal form to POST a new book to the catalog.

Borrow/Return: Buttons on each book card to PATCH the available_copies.

Edit/Update: A modal with two update options:

PATCH (Edit): For partial updates (e.g., changing only the title).

PUT (Replace): For replacing the entire book record with new data.

Delete Book: A DELETE request to remove a specific book.

Delete All Books: A DELETE request to clear the entire catalog.

Status Messages: A non-blocking alert box provides success or error feedback.

⚙️ Backend Features (main.py)

The API provides the core logic and data storage:

Manage a collection of books stored in memory.

Health-check endpoint to verify server status.

Display all books.

Retrieve a specific book by its ID.

Add new books.

Update book data fully (PUT) or partially (PATCH).

Borrow a book (decrease available_copies).

Return a book (increase available_copies).

Delete individual books or all books at once.

🗂️ Project Structure

main.py: The FastAPI backend server. Contains all API logic and data.

library_manager.html: The single-page frontend application (HTML/Tailwind CSS/JS).

🚀 Getting Started

You must run both parts at the same time for the application to work.

Prerequisites

Python 3.7+

pip (Python package installer)

1. Run the Backend (API Server)

Install dependencies:

# Install FastAPI and the Uvicorn server
pip install "fastapi[all]" uvicorn


Start the server:
From your terminal (in the same directory as main.py), run:

uvicorn main:server --reload


The API will be available at: http://127.0.0.1:8000

Interactive API docs (Swagger UI): http://127.0.0.1:8000/docs

Alternative docs (ReDoc): http://127.0.0.1:8000/redoc

2. Run the Frontend (Webpage)

Open the library_manager.html file in your code editor.

Click the "Preview" button in your editor.

The webpage is configured in its JavaScript to send all requests to http://127.0.0.1:8000, so it will automatically connect to your running backend.

🔌 API Documentation

Data Models

The API uses Pydantic models to validate request data.

new_book

Used for POST (Add) and PUT (Replace). All fields are required.

class new_book(BaseModel):
    id: int
    title: str
    Author: str
    available_copies: int


new_updated_book

Used for PATCH (Edit). All fields are optional.

class new_updated_book(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    Author: Optional[str] = None
    available_copies: Optional[int] = None


Endpoints

Health Check

GET /

Description: Check if the server is running.

Response (200 OK):

{
  "health": "OK",
  "status": "success"
}


Get All Books

GET /books

Description: Return all books from the in-memory dictionary.

Response (200 OK):

{
  "books": {
    "1": {
      "id": 1,
      "title": "The Great Gatsby",
      "Author": "F.Scott Fitzgerald",
      "available_copies": 6
    },
    "2": {
      "id": 2,
      "title": "1984",
      "Author": "George Orwell",
      "available_copies": 4
    }
  },
  "status": "success"
}


Get a Specific Book

GET /books/{id}

Path Parameter: id (int) – The ID of the book to retrieve.

Description: Return a single book by its ID.

Success Response (200 OK):

{
  "id": 1,
  "title": "The Great Gatsby",
  "Author": "F.Scott Fitzgerald",
  "available_copies": 6
}


Error Response (404 Not Found):

{
  "detail": "Book not found"
}


Add a New Book

POST /books/{id}

Path Parameter: id (int) – Present in the path but ignored by the logic. A new ID is generated automatically.

Body: new_book JSON (all fields required).

Note: The function assigns new_id = max(books.keys()) + 1.

Success Response (200 OK):

{
  "book": {
    "id": 5,
    "title": "New Book Title",
    "Author": "Author Name",
    "available_copies": 5
  },
  "status": "added successfully!"
}


Replace All Details of a Book (Full Update)

PUT /books/{id}

Path Parameter: id (int) – The ID of the book to replace.

Body: new_book JSON (all fields required).

Description: Replaces the entire book object for the given ID.

Success Response (200 OK):

{
  "book": {
    "id": 1,
    "title": "Updated Title",
    "Author": "Updated Author",
    "available_copies": 7
  },
  "status": "updated successfully!"
}


Error Response (404 Not Found):

{
  "detail": "Book not found"
}


Partially Update a Book (Partial Edit)

PATCH /books/{id}

Path Parameter: id (int) – The ID of the book to update.

Body: new_updated_book JSON (any field is optional).

Description: Updates only the provided fields. Unset fields remain unchanged.

Success Response (200 OK):

{
  "book": {
    "id": 1,
    "title": "Partially Updated Title",
    "Author": "F.Scott Fitzgerald",
    "available_copies": 10
  },
  "status": "details edited successfully!"
}


Error Response (404 Not Found):

{
  "detail": "Book not found"
}


Borrow a Book

PATCH /books/{id}/borrow

Path Parameter: id (int) – The ID of the book to borrow.

Description: Decreases available_copies by 1.

Success Response (200 OK):

{
  "book": {
    "id": 1,
    "title": "The Great Gatsby",
    "Author": "F.Scott Fitzgerald",
    "available_copies": 5
  },
  "status": "book borrowed successfully!"
}


Error Response (400 Bad Request):

{
  "detail": "No copies available to borrow"
}


Return a Book

PATCH /books/{id}/return

Path Parameter: id (int) – The ID of the book to return.

Description: Increases available_copies by 1.

Success Response (200 OK):

{
  "book": {
    "id": 1,
    "title": "The Great Gatsby",
    "Author": "F.Scott Fitzgerald",
    "available_copies": 7
  },
  "status": "book returned successfully!"
}


Error Response (404 Not Found):

{
  "detail": "Book not found"
}


Delete a Specific Book

DELETE /books/{id}

Path Parameter: id (int) – The ID of the book to delete.

Description: Deletes a single book by its ID.

Success Response (200 OK):

{
  "book": {
    "id": 1,
    "title": "The Great Gatsby",
    "Author": "F.Scott Fitzgerald",
    "available_copies": 6
  },
  "status": "book deleted successfully!"
}


Error Response (404 Not Found):

{
  "detail": "Book not found"
}


Delete All Books

DELETE /books

Description: Deletes all books from the in-memory dictionary.

Success Response (200 OK):

{
  "books": {},
  "status": "all books deleted successfully!"
}


📋 Examples (cURL)

You can test the API from your terminal using curl.

Example: Fetch All Books

curl [http://127.0.0.1:8000/books](http://127.0.0.1:8000/books)


Example: Add a New Book

curl -X POST "[http://127.0.0.1:8000/books/0](http://127.0.0.1:8000/books/0)" \
 -H "Content-Type: application/json" \
 -d '{
   "id": 10,
   "title": "Example Book",
   "Author": "Example Author",
   "available_copies": 2
 }'


Example: Borrow Book 1

curl -X PATCH [http://127.0.0.1:8000/books/1/borrow](http://127.0.0.1:8000/books/1/borrow)


Example: Delete Book 1

curl -X DELETE [http://127.0.0.1:8000/books/1](http://127.0.0.1:8000/books/1)