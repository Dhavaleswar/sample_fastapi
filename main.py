import pandas as pd
from fastapi import FastAPI
import datetime as dt
import uvicorn
import socket
import logging
from typing import List, Dict
from pydantic import BaseModel
import random
import numpy as np

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

class MarksInput(BaseModel):
    names: List[str]
    subjects: List[str]


class SubjectMarks(BaseModel):
    marks: Dict[str, Dict[str, int]]


@app.post("/marks")
def get_student_marks(inputs : MarksInput) -> SubjectMarks:
    subjects = ['A', 'B', 'C', 'D', 'E', 'F']
    df = pd.DataFrame(
        np.random.randint(30, 100, size=(len(inputs.names), len(subjects))),
        index = inputs.names,
        columns = subjects,
    )

    return SubjectMarks(marks=df[inputs.subjects].to_dict())


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000)
