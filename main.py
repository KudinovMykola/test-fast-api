from fastapi import FastAPI, Query, Path, Body
from schemas import Author, Book, BookModel
from typing import List

BOOK_APP_HOOK = '/book'

app = FastAPI()


@app.get('/')
def home() -> dict:
    return dict(key='hello')


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)) -> dict:
    return dict(author=author)


@app.post(BOOK_APP_HOOK)
def update_book(item: Book, author: Author, quantity: int = Body(...)) -> dict:
    return dict(item=item, author=author, quantity=quantity)


# @app.put(
#     BOOK_APP_HOOK,
#     response_model=Book,
#     response_model_exclude_unset=True,
#     response_model_exclude={'pages', 'date'}
# )
@app.put(BOOK_APP_HOOK, response_model=BookModel)
def create_book(item: Book):
    return BookModel(**item.dict(), id=8)


@app.get(BOOK_APP_HOOK)
def get_book(q: List[str] = Query(..., description='Search Book')) -> List[str]:
    return q


@app.get(f"{BOOK_APP_HOOK}/{{pk}}")
def get_some_book(
        pk: int = Path(..., gte=1, le=20),
        pages: int = Query(None, gt=10, le=500)
) -> dict:

    # The same that
    # book = item.dict()
    # book['id'] = 3
    # return book
    return dict(pk=pk, pages=pages)


@app.get('/{pk}')
def get_item(pk: int, q: int = None) -> dict:
    return dict(key=pk, q=q)


@app.get('/user/{pk}/items/{item}')
def get_item(pk: int, item: str) -> dict:
    return dict(user=pk, item=item)
