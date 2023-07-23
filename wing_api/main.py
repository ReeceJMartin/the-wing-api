# from wing_api.resources.greeting import Greeting
from fastapi import FastAPI
from typing import Union

from routers import greeting

app = FastAPI()


app.include_router(greeting.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q + " is your message"}
