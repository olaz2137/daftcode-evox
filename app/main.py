from fastapi import FastAPI
from app import schemas, models
from app.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/post')
def create(request: schemas.Text ):
    return request