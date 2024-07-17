from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = 'App with FastAPI'
app.version = '0.0.1'

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['Hola mundo HTMLResponse'])
def message():
    return HTMLResponse('<h1>Hola mundo</h1>')

@app.get('/hello-world', tags=['Hola mundo normal'])
def helloWorld():
    return 'Hola Mundo (String)'

@app.get('/movies', tags=['Movies'])
def getMovies():
    return movies


@app.get("/movies/{id}")
def read_item(id: int):
    return {"movie_id": id}