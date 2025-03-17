from pydantic import BaseModel, Field
from datetime import date


class Book(BaseModel):
    name: str | None = Field(None, example="1984")
    author: str | None = Field(None, example="George Orwell")
    time: date | None = Field(default_factory=date.today)  #
