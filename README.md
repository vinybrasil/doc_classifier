# Deploying a classification model on AWS Lambda with Docker and FastAPI

Create and deploy a model to classify selfies and IDs photos on AWS Lambda with Tensorflow, FastAPI and Docker. The entire explation of the projects can be found at my [blog post](https://vinybrasil.github.io/portfolio/classificationmodel/).

To run the api:

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("doc_classifier.main:app", host="0.0.0.0", port=8000, reload=True)
```

To test it with Python:
```python
import base64
import json
import requests

encoded_string = base64.b64encode(open("experiments/test_doc_2.jpg", "rb").read())
encoded_string_utf = encoded_string.decode("utf-8")

print(
     requests.post(
         "http://localhost:8000/classifier",
         json={"input_photo": encoded_string_utf, "leadId": "f8cad38c-c4f3-4f50-ab23-5262033bfef1"},
     ).text
 )```

