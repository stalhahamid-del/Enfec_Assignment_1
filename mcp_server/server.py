from fastapi import FastAPI

app = FastAPI()

MOCK_DATA = {
    "what is the capital of france?": "Paris is the capital of France.",
    "what is the capital of india?": "New Delhi is the capital of India.",
    "what is the capital of usa?": "Washington, D.C is the capital of USA.",
}

@app.get("/search")
def search(query: str):
    return {
        "query": query,
        "result": MOCK_DATA.get(query.lower(), "No result found.")
    }