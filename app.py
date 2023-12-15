from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def root():
    return HTMLResponse(
        """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Фоновое изображение</title>
  <style type="text/css">
   BODY {
    background: url(images/target.gif) no-repeat 30px 20px; /* Параметры фона */
   }
  </style>
 </head>
 <body>
  <p>...</p>
 </body>
</html>"""
    )
