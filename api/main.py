import json
from base64 import b64encode

from fastapi import FastAPI
from objects.output import OutputPrediction
from predictor.make_prediction import load_model, predict

app = FastAPI()

import base64
import io

from PIL import Image


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.post("/classifier/")
def classifier(a: dict):
    # input_photo: bytes, leadId: str
    # print(a)

    # photo = a["input_photo"]
    # print(type(b'{photo}'))

    # image_data = a['input_photo'].encode()
    # image = Image.open(io.BytesIO(b'a["input_photo"]'))
    # image.show()
    # image_data = a['input_photo'].encode()
    # print(image_data)
    image_bytes = base64.b64decode(a["input_photo"])
    #load_model()
    predict(image_bytes)
    # image = Image.open(io.BytesIO(image_bytes))

    # image.show()
    return {"Ping": "Pong"}
