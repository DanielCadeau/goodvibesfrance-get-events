from fastapi import FastAPI
from .fetch import cinemas

app = FastAPI()

@app.get("/")
def read_root():
    return {"Good Vibes France": "Hello World! 🤗 This API is used to feel good vibes in France. You can find documentation here: api.goodvibesfrance.live/redoc"}

@app.get("/cinemas/{city}")
async def read_events(city):
    data = {
        "cinemas": await cinemas.list(city)
    }
    return data