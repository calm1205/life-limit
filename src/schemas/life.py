from pydantic import BaseModel


class LifeQueryParams(BaseModel):
    year: int
    month: int
    day: int
