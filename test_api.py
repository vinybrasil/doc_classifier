import base64

import requests

print(requests.get("http://localhost:8000/").text)

encoded_string = base64.b64encode(open("test_pic.jpg", "rb").read())
encoded_string_utf = encoded_string.decode("utf-8")

print(requests.get("http://localhost:8000/").text)

print(
    requests.post(
        "http://localhost:8000/classifier/",
        json={"input_photo": encoded_string_utf, "leadId": "123"},
    ).text
)


# image_bytes = base64.b64decode(encoded_string_utf)

# image = Image.open(io.BytesIO(image_bytes))
# image.show()
