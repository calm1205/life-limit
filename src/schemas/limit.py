from pydantic import BaseModel

class LimitQueryParams(BaseModel):
    year: int
    month: int
    day: int