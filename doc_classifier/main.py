from typing import Optional

from fastapi import FastAPI

from doc_classifier.objects.output import OutputPrediction
from doc_classifier.predictor.make_prediction import predict

app = FastAPI()


@app.get("/health_check/")
def read_root():
    return {"Ping": "Pong"}


@app.post("/classifier/")
def classifier(a: Optional[dict]):
    return OutputPrediction(
        leadId=a["leadId"], photoHash="a", prediction=predict(a["input_photo"])
    )
