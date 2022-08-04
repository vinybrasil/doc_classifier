from mangum import Mangum
from doc_classifier.main import app

lambda_handler = Mangum(app, lifespan="off")