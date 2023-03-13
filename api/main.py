from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Score(BaseModel):
    slope: int
    par: int
    total_score: int

@app.get("/")
async def index():
    return {"message": "Hello World!"}

@app.post('/scores', status_code=201)
async def create_score(score_data: Score):
    return {
        "slope": score_data.slope,
        "par": score_data.par,
        "total_score": score_data.total_score
    }