from fastapi import FastAPI
from .fetch import cinemas, festivals

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Good Vibes France": "Hello World! 🤗 This API is used to feel good vibes in France.",
        "Documentation": "You can find documentation here: http://api.goodvibesfrance.live/redoc",
        "Details": "This is a school project developed by 3 students of Epitech, Paris. The goal of this project is to create a platform where people can feel good vibes in France. We don't use data for commercial purposes, but we use it to make the platform more interesting. We hope you enjoy it!",
        "Contact": "Please reach out if you want to remove your data from the platform or if you have any questions.",
        "Email": {
            "Daniel Cadeau - developer of this api": "daniel1.cadeau@epitech.eu",
        },
        "Source": "http://api.goodvibesfrance.live/source",
    }

@app.get("/source")
def read_source():
    return {
        "Github": "https://github.com/DanielCadeau/goodvibesfrance-get-events"
    }

@app.get("/cinemas/{city}")
async def read_cinemas(city):
    data = {
        "cinemas": await cinemas.fetch(city)
    }
    return data

@app.get("/festivals")
async def read_festivals():
    return await festivals.fetch()