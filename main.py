from fastapi import FastAPI
from typing import Union
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'App with FastAPI'
app.version = '0.0.1'

@app.get('/', tags=['Hola mundo HTMLResponse'])
def message():
    return HTMLResponse('<h1>Hola mundo</h1>')

@app.get('/hello-world', tags=['Hola mundo normal'])
def helloWorld():
    return 'Hola Mundo (String)'

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}