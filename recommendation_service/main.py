# recommendation_service/main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/recommend")
def recommend():
    return {"books": ["The Alchemist", "Sapiens"]}
