import numpy as np
import tensorflow as tf
from PIL import Image
import os
import joblib
import base64
import io

tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
def load_model():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    thefile = os.path.join(package_dir, "resources\model_v2")
    #print(thefile)
    #model = joblib.load(thefile)
    model = joblib.load("D:\\projects\\portfolio\\doc_classifier\\api\\predictor\\resources\\model_v2")
    return model 

def bytes_to_array(image_b64):
    image_bytes = base64.b64decode(image_b64)
    image = Image.open(io.BytesIO(image_bytes))
    return np.asarray(image)


def predict(image_b64):
    model = load_model()
    print(bytes_to_array(image_b64))
    
    #print(bytes_to_array(image))
