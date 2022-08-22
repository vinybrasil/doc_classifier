from typing import Optional

from fastapi import FastAPI

from doc_classifier.objects.output import OutputPrediction
from doc_classifier.predictor.make_prediction import predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"VAMOS": "FLAMENGO"}

@app.get("/health_check")
def read_root():
    return {"Ping": "Pong"}

@app.post("/classifier")
def classifier(req: Optional[dict]):
    prediction = predict(req["input_photo"])
    return OutputPrediction(
        leadId=req["leadId"], photoHash=prediction[1], prediction=prediction[0]
    )


