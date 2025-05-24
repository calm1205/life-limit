from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
      <body>
        <h1>Hello World</h1>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health")
def health():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}