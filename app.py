from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def root():
    with open('coming_soon.html') as src:
        data = src.read()
    return HTMLResponse(content=data, media_type='text/html')
