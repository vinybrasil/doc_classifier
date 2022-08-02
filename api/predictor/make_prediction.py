import base64
import io
import os

import numpy as np
import tensorflow as tf
from PIL import Image
from scipy.special import softmax

from api.objects.output import Prediction, RawPrediction, ProbabilitiesPrediction


SIZE = 64


def load_model():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    thefile = os.path.join(package_dir, "resources\model_v6")
    model = tf.keras.models.load_model(thefile)
    return model


def bytes_to_array(image_b64):
    image_decoded = base64.b64decode(image_b64)
    image = Image.open(io.BytesIO(image_decoded))
    return np.asarray(image)


def prepare_image(img):
    img_gray = tf.image.rgb_to_grayscale(img)
    image_resized = tf.image.resize(img_gray, (SIZE, SIZE))
    return np.asarray(image_resized).reshape(1, SIZE, SIZE, 1)


def predict(image_b64):
    model = load_model()
    image_as_array = bytes_to_array(image_b64)
    image_ready = prepare_image(image_as_array)
    raw_prediction = model.predict(image_ready)
    class_predicted = "selfie" if (softmax(raw_prediction[0])[0] > softmax(raw_prediction[0])[1]) else "document"

    prediction = Prediction(raw_prediction =  RawPrediction(selfie_score=list(raw_prediction[0])[0], 
                                                            document_score= list(raw_prediction[0])[1]), 
                            probabilities = ProbabilitiesPrediction(selfie_probability =list(softmax(raw_prediction[0]))[0], 
                                                                    document_probability= list(softmax(raw_prediction[0]))[1]),
                            class_predicted = class_predicted) 
    return prediction