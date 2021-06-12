from datetime import date
from typing import List

from pydantic import BaseModel, validator, Field


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(max_length=2)
    last_name: str
    age: int = Field(..., gt=12, lt=20, description='How old is he')

    # @validator('age')
    # def check_age(cls, v):
    #     limit = 15
    #     if v < limit:
    #         raise ValueError(f'Requires greater than or equal to 15 {limit}')
    #     return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []

    pages: int


class BookModel(Book):
    id: int = 1
