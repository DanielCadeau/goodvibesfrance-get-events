from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Good Vibes France": "Hello World! 🤗 This API is used to get events in France."}

@app.get("/events")
def read_events():
    return {"events": "all"}