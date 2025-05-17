from fastapi import FastAPI, Request
from summarizer import summarize_text
from search_engine import get_similar_posts

app = FastAPI()

@app.post("/analyze/")
async def analyze_deck(payload: dict):
    deck = payload.get("deck")
    context = get_similar_posts(deck)
    summary = summarize_text(context)
    return {"summary": summary}
