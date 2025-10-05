from fastapi import FastAPI
import datetime as dt
import uvicorn
import socket
import logging

app = FastAPI()

logger = logging.getLogger()

@app.get("/hi")
def hello_word():
    logger.info("User said hi")
    return "Hi Babu"

@app.get("/wishes")
def wish_me(name:str):
    logger.info("User sending wishes")
    return {
        "message": f"Hello {name}",
        "time": dt.datetime.now().strftime("%Y-%m-%d %H:%m:%s")
    }
