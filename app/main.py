from fastapi import FastAPI
from .fetch import cinemas, festivals

app = FastAPI()

@app.get("/")
def read_root():
    return {"Good Vibes France": "Hello World! 🤗 This API is used to feel good vibes in France. You can find documentation here: api.goodvibesfrance.live/redoc"}

@app.get("/cinemas/{city}")
async def read_cinemas(city):
    data = {
        "cinemas": await cinemas.fetch(city)
    }
    return data

@app.get("/festivals")
async def read_festivals():
    return await festivals.fetch()