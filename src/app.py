from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()


class PredictionRequest(BaseModel):
    features: list


@app.get("/")
def root():
    return {"status": "Iris classifier is running"}


@app.post("/predict")
def make_prediction(request: PredictionRequest):
    result = predict(request.features)
    return {"prediction": result}
