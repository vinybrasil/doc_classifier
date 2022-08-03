from mangum import Mangum
from doc_classifier.main import app
#def lambda_handler(event, context):
#    return event, context

lambda_handler = Mangum(app)