from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.search_pipeline import run_search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "API Running"
    }


@app.get("/search")
def search(query: str):

    return run_search(query)