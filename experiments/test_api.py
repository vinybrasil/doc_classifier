import base64
import json
import requests

encoded_string = base64.b64encode(open("test_doc_2.jpg", "rb").read())
encoded_string_utf = encoded_string.decode("utf-8")

print(
     requests.post(
         "http://localhost:8000/classifier",
         json={"input_photo": encoded_string_utf, "leadId": "f8cad38c-c4f3-4f50-ab23-5262033bfef1"},
     ).text
 )
