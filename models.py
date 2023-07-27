from pydantic import BaseModel, Field, HttpUrl
from typing import Sequence

# from datetime import datetime
# from uuid import UUID, uuid4
# from enum import Enum


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


# class Gender(str, Enum):
#     male = "male"
#     female = "female"


# class Role(str, Enum):
#     admin = "admin"
#     user = "user"
#     base = "base"


# class User(BaseModel):
#     id: UUID = Field(default_factory=uuid4)
#     created: datetime = Field(default_factory=datetime.utcnow)
#     first_name: str
#     last_name: str
#     age: int
#     fav_color: str | None
#     gender: Gender
#     roles: list[Role]
