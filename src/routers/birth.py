from fastapi import APIRouter
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    current_year = datetime.now().year
    return templates.TemplateResponse(request=request, name="birth.html", context={"current_year": current_year})


@router.post("/")
def create_birth(year: int = Form(...), month: int = Form(...), day: int = Form(...)):
    print(year, month, day)
    return {"Hello": "World"}
