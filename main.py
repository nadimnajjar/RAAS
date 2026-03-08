from fastapi import FastAPI
from fastapi import Response
from roasts import ROAST
import random


app= FastAPI()

@app.get("/")
def roast():
    return {"roast": random.choice(ROAST)}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)
