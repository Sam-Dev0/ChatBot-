#Para Correrlo usar python -m uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import wordnet 

nltk.data.path.append(r'C:\Users\usuario\chatbot\Dataset')

nltk.download('punkt')
nltk.download('wordnet')

def load_movies():
    movies_df = pd.read_csv('Dataset/netflix_titles.csv')[['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']]
    movies_df.columns = ['id', 'type', 'title', 'director', 'cast', 'country', 'date added', 'release year', 'rating', 'duration', 'category', 'overview']
    return movies_df.fillna('').to_dict(orient='records')
    
movie_list = load_movies()

def get_synonymus(word):
    return {lemma.name().lower() for syn in wordnet.synsets(word) for lemma in syn.lemmas()}

app = FastAPI(title="Movie Recommendation API", version="1.0.0")

@app.get('/', tags=['Home'])
def home():
    return HTMLResponse(content="<h1>Welcome to the Movie Recommendation API</h1>", status_code=200)

@app.get('/movies', tags=['Movies'])
def get_movies():
    if not movie_list:
        raise HTTPException(status_code=500, detail="Error fetching movies")
    return movie_list

@app.get('/movies/{movie_id}', tags=['Movies'])
def get_movie(movie_id: str):
    movie = next((movie for movie in movie_list if movie['id'] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.get('/chatbot', tags=['Chatbot'])
def chatbot(query: str):
    query_words = word_tokenize(query.lower())
    synonymus = {word for q in query_words for word in get_synonymus(q)} | set(query_words)
    
    results = [m for m in movie_list if any(s in m['category'].lower() for s in synonymus)]

    return JSONResponse(content={
        "results": results, 
        "status": "200 OK" if results else "404 Not Found", 
        "count": len(results)
    })

@app.get('/movies/search/category', tags=['Movies'])
def get_movies_by_category(category: str):
    return [m for m in movie_list if category.lower() in m['category'].lower()]