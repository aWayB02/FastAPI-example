from fastapi import APIRouter, HTTPException
from .shemas import Book
from uuid import uuid4
from typing import Dict


books = {}
routes = APIRouter()


@routes.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Hero API!"}


@routes.get(
    "/get_books",
    description="Return all books",
    tags=["books"],
    response_description="Will return all books in json format",
    # responses={
    #     200: {
    #         "description": "Successful response",
    #         "content": {
    #             "application/json": {
    #                 "example": {
    #                     "21fc7cb6-e9c8-48f8-98ab-09240062fb9c": {
    #                         "name": "1984",
    #                         "author": "George Orwell",
    #                         "time": "2025-03-17",
    #                     },
    #                 }
    #             }
    #         },
    #     }
    # },
)
def get_books() -> Dict[str, dict]:
    return books


@routes.get(
    "/get_book/{id}",
    description="Return book by id",
    response_description="Will return book in json format by id",
    tags=["books"],
)
def get_book(id: str) -> Dict[str, dict]:
    if id in books:
        return books[id]
    raise HTTPException(status_code=404, detail="book not found")


@routes.post(
    "/add_book",
    description="Add a book to the database",
    response_description="Returns a JSON response indicating success",
    tags=["books"],
    status_code=201,
)
def add_book(book: Book) -> dict:
    id_book = str(uuid4())
    books[id_book] = {
        "name": book.name,
        "author": book.author,
        "time": book.time,
    }
    return {"status": "success", "id": id_book, "message": "Book added successfully"}


@routes.delete(
    "/delete_books/{id}",
    description="Delete the book from the database",
    response_description="Returns a JSON response indicating success",
    tags=["books"],
    status_code=204,
)
def delete_books(id: str):
    if books.get(id, False):
        books.pop(id)
        return {
            "status": "success",
            "message": f"the book with this id {id} has been deleted",
        }
    raise HTTPException(status_code=404, detail="book not found")


@routes.put(
    "/update_book/{id}",
    description="Update the book in the database",
    response_description="Returns a JSON response indicating success",
    tags=["books"],
)
def update_book(id: str, book: Book):
    if id in books:
        books[id].update({k: v for k, v in book.dict().items() if v is not None})
    raise HTTPException(status_code=404, detail="book not found")
