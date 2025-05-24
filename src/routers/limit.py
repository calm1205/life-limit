from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from datetime import date

from src.schemas.limit import LimitQueryParams
from src.libs.calculate_age import calculate_age
from src.libs.days_until_90 import days_until_90

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request, params: LimitQueryParams = Depends(LimitQueryParams)):
    birth_date = date(params.year, params.month, params.day)
    age = calculate_age(birth_date)
    until_days = days_until_90(birth_date)
    return templates.TemplateResponse(request=request, name="limit.html", context={"params": params, "age": age, "until_days": until_days})