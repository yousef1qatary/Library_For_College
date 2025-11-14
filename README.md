# 📚 FastAPI Library Manager

A full-stack web application for managing a simple library catalog.

* **Backend:** FastAPI (Python)
* **Frontend:** Single-page HTML/CSS/JavaScript
* **Storage:** In-memory Python dictionary

The project demonstrates CRUD operations (Create, Read, Update, Delete) and special actions like borrowing and returning books.

github Pages Link:
## https://yousef1qatary.github.io/Library_For_College/



---

## 📑 Table of Contents

* [Features](#-features)
* [Frontend Features](#-frontend-features)
* [Backend Features](#️-backend-features)
* [Project Structure](#️-project-structure)
* [Getting Started](#-getting-started)

  * [Prerequisites](#prerequisites)
  * [1. Run the Backend](#1-run-the-backend-api-server)
  * [2. Run the Frontend](#2-run-the-frontend-webpage)
* [API Documentation](#-api-documentation)

  * [Data Models](#data-models)
  * [Endpoints](#endpoints)
* [Examples (cURL)](#-examples-curl)
* [Future Improvements](#-future-improvements)

---

# ✨ Features

## ✨ Frontend Features (`library_manager.html`)

The user interface provides:

* **View All Books** — Fetches and displays all books.
* **Add New Book** — Modal form for creating a book.
* **Borrow / Return** — Buttons modify `available_copies`.
* **Edit / Update Book**

  * `PATCH` for partial update.
  * `PUT` for full replacement.
* **Delete Book** — Removes a specific item.
* **Delete All Books** — Clears the entire catalog.
* **Status Messages** — Non-blocking alerts for feedback.

---

## ⚙️ Backend Features (`main.py`)

The backend API supports:

* In-memory book storage.
* Health check endpoint.
* Fetch all books.
* Retrieve a single book.
* Add new books.
* Update or partially update existing books.
* Borrow / return functionality.
* Delete individual or all books.

---

# 🗂️ Project Structure

```
project/
│── main.py                 # FastAPI backend
│── library_manager.html    # Frontend page
│── README.md               # Documentation
```

---

# 🚀 Getting Started

You must run both the backend and frontend.

---

## Prerequisites

* Python **3.7+**
* `pip`

---

## 1. Run the Backend (API Server)

### Install Dependencies

```bash
pip install "fastapi[all]" uvicorn
```

### Start the Server

Run inside the same directory as `main.py`:

```bash
uvicorn main:server --reload
```

### Access URLs

* API root → [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc docs → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 2. Run the Frontend (Webpage)

1. Open **library_manager.html** in your editor.
2. Click **Preview**, or open it directly in your browser.
3. It automatically connects to `http://127.0.0.1:8000`.

---

# 🔌 API Documentation

---

## Data Models

### `new_book` (used for POST + PUT)

```python
class new_book(BaseModel):
    id: int
    title: str
    Author: str
    available_copies: int
```

All fields are **required**.

---

### `new_updated_book` (used for PATCH)

```python
class new_updated_book(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    Author: Optional[str] = None
    available_copies: Optional[int] = None
```

All fields are **optional**.

---

# Endpoints

## 🩺 Health Check

### `GET /`

**200 OK**

```json
{
  "health": "OK",
  "status": "success"
}
```

---

## 📚 Get All Books

### `GET /books`

**Returns all books.**

```json
{
  "books": {
    "1": {
      "id": 1,
      "title": "The Great Gatsby",
      "Author": "F.Scott Fitzgerald",
      "available_copies": 6
    }
  },
  "status": "success"
}
```

---

## 📘 Get a Specific Book

### `GET /books/{id}`

**200 OK**

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "Author": "F.Scott Fitzgerald",
  "available_copies": 6
}
```

**404 Not Found**

```json
{ "detail": "Book not found" }
```

---

## ➕ Add a New Book

### `POST /books/{id}`

*(Path ID is ignored; system auto-assigns new ID)*

**Request Body**

```json
{
  "id": 10,
  "title": "Example",
  "Author": "Author Name",
  "available_copies": 3
}
```

**200 OK**

```json
{
  "book": { ... },
  "status": "added successfully!"
}
```

---

## ✏️ Replace Entire Book

### `PUT /books/{id}`

**Full replacement (requires all fields).**

---

## 🩹 Partially Update Book

### `PATCH /books/{id}`

**Updates only the given fields.**

```json
{
  "title": "Updated Title"
}
```

---

## 📕 Borrow a Book

### `PATCH /books/{id}/borrow`

**Success**

```json
{
  "status": "book borrowed successfully!"
}
```

**Error**

```json
{ "detail": "No copies available to borrow" }
```

---

## 📘 Return a Book

### `PATCH /books/{id}/return`

```json
{
  "status": "book returned successfully!"
}
```

---

## 🗑️ Delete a Book

### `DELETE /books/{id}`

**Deletes a single book.**

---

## 🧹 Delete All Books

### `DELETE /books`

```json
{
  "books": {},
  "status": "all books deleted successfully!"
}
```

---

# 📋 Examples (cURL)

---

### Get All Books

```bash
curl http://127.0.0.1:8000/books
```

---

### Add a New Book

```bash
curl -X POST "http://127.0.0.1:8000/books/0" \
-H "Content-Type: application/json" \
-d '{
  "id": 10,
  "title": "Example Book",
  "Author": "Example Author",
  "available_copies": 2
}'
```

---

### Borrow Book 1

```bash
curl -X PATCH http://127.0.0.1:8000/books/1/borrow
```

---

### Delete Book 1

```bash
curl -X DELETE http://127.0.0.1:8000/books/1
```

---
