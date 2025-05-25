from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from datetime import date

from src.schemas.life import LifeQueryParams
from src.libs.calculate_age import calculate_age
from src.libs.days_until_90 import days_until_90

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def read_root(request: Request, params: LifeQueryParams = Depends(LifeQueryParams)):
    birth_date = date(params.year, params.month, params.day)
    age = calculate_age(birth_date)
    passed_days = (date.today() - birth_date).days
    passed_months = passed_days // 30
    passed_weeks = passed_days // 7

    until_days = days_until_90(birth_date)
    until_months = until_days // 30
    until_weeks = until_days // 7

    return templates.TemplateResponse(
        request=request,
        name="life.html",
        context={
            "params": params,
            "age": age,
            "passed_days": passed_days,
            "passed_months": passed_months,
            "passed_weeks": passed_weeks,
            "until_days": until_days,
            "until_months": until_months,
            "until_weeks": until_weeks,
        },
    )
