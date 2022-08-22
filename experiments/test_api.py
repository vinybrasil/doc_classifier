import base64
import json
import requests

encoded_string = base64.b64encode(open("test_doc_2.jpg", "rb").read())
encoded_string_utf = encoded_string.decode("utf-8")

print(
     requests.post(
         "http://localhost:8000/classifier",
        # "https://k1udh87ek6.execute-api.us-east-1.amazonaws.com/classifier",
         json={"input_photo": encoded_string_utf, "leadId": "f8cad38c-c4f3-4f50-ab23-5262033bfef1"},
     ).text
 )

# '''





# d = {
#   "body": "eyJ0ZXN0IjoiYm9keSJ9", #{"test":"body"} em base64 HAHAHAHAHAHAHAHAHAHAHAHA
#   "resource": "/{proxy+}",
#   "path": "/health_check/",
#   "httpMethod": "GET",
#   "isBase64Encoded": True,
#   "queryStringParameters": {
#     "foo": "bar"
#   },
#   "multiValueQueryStringParameters": {
#     "foo": [
#       "bar"
#     ]
#   },
#   "pathParameters": {
#     "proxy": "/path/to/resource"
#   },
#   "stageVariables": {
#     "baz": "qux"
#   },
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch",
#     "Accept-Language": "en-US,en;q=0.8",
#     "Cache-Control": "max-age=0",
#     "CloudFront-Forwarded-Proto": "https",
#     "CloudFront-Is-Desktop-Viewer": "true",
#     "CloudFront-Is-Mobile-Viewer": "false",
#     "CloudFront-Is-SmartTV-Viewer": "false",
#     "CloudFront-Is-Tablet-Viewer": "false",
#     "CloudFront-Viewer-Country": "US",
#     "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Custom User Agent String",
#     "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
#     "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
#     "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
#     "X-Forwarded-Port": "443",
#     "X-Forwarded-Proto": "https"
#   },
#   "multiValueHeaders": {
#     "Accept": [
#       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
#     ],
#     "Accept-Encoding": [
#       "gzip, deflate, sdch"
#     ],
#     "Accept-Language": [
#       "en-US,en;q=0.8"
#     ],
#     "Cache-Control": [
#       "max-age=0"
#     ],
#     "CloudFront-Forwarded-Proto": [
#       "https"
#     ],
#     "CloudFront-Is-Desktop-Viewer": [
#       "true"
#     ],
#     "CloudFront-Is-Mobile-Viewer": [
#       "false"
#     ],
#     "CloudFront-Is-SmartTV-Viewer": [
#       "false"
#     ],
#     "CloudFront-Is-Tablet-Viewer": [
#       "false"
#     ],
#     "CloudFront-Viewer-Country": [
#       "US"
#     ],
#     "Host": [
#       "0123456789.execute-api.us-east-1.amazonaws.com"
#     ],
#     "Upgrade-Insecure-Requests": [
#       "1"
#     ],
#     "User-Agent": [
#       "Custom User Agent String"
#     ],
#     "Via": [
#       "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
#     ],
#     "X-Amz-Cf-Id": [
#       "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
#     ],
#     "X-Forwarded-For": [
#       "127.0.0.1, 127.0.0.2"
#     ],
#     "X-Forwarded-Port": [
#       "443"
#     ],
#     "X-Forwarded-Proto": [
#       "https"
#     ]
#   },
#   "requestContext": {
#     "accountId": "123456789012",
#     "resourceId": "123456",
#     "stage": "prod",
#     "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
#     "requestTime": "09/Apr/2015:12:34:56 +0000",
#     "requestTimeEpoch": 1428582896000,
#     "identity": {
#       "cognitoIdentityPoolId": None,
#       "accountId": None,
#       "cognitoIdentityId": None,
#       "caller": None,
#       "accessKey": None,
#       "sourceIp": "127.0.0.1",
#       "cognitoAuthenticationType": None,
#       "cognitoAuthenticationProvider": None,
#       "userArn": None,
#       "userAgent": "Custom User Agent String",
#       "user": None
#     },
#     "path": "/prod/path/to/resource",
#     "resourcePath": "/{proxy+}",
#     "httpMethod": "POST",
#     "apiId": "1234567890",
#     "protocol": "HTTP/1.1"
#   }
# }

# print(
#     requests.post("http://localhost:9000/2015-03-31/functions/function/invocations", json=d).text)


# a = base64.urlsafe_b64encode(json.dumps({"leadId": "95ac13c6-10c8-4c17-83f7-ba8201429be9",
#     "input_photo": encoded_string_utf}).encode()).decode()

# #d = {
#   "body": a,

#   "resource": "/{proxy+}",
#   "path": "/classifier/",
#   "httpMethod": "POST",
#   "isBase64Encoded": True,
#   "queryStringParameters": {
#   },
#   "multiValueQueryStringParameters": {
#     "foo": [
#       "bar"
#     ]
#   },
#   "pathParameters": {
#     "proxy": "/path/to/resource"
#   },
#   "stageVariables": {
#     "baz": "qux"
#   },
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch",
#     "Accept-Language": "en-US,en;q=0.8",
#     "Cache-Control": "max-age=0",
#     "CloudFront-Forwarded-Proto": "https",
#     "CloudFront-Is-Desktop-Viewer": "true",
#     "CloudFront-Is-Mobile-Viewer": "false",
#     "CloudFront-Is-SmartTV-Viewer": "false",
#     "CloudFront-Is-Tablet-Viewer": "false",
#     "CloudFront-Viewer-Country": "US",
#     "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Custom User Agent String",
#     "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
#     "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
#     "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
#     "X-Forwarded-Port": "443",
#     "X-Forwarded-Proto": "https"
#   },
#   "multiValueHeaders": {
#     "Accept": [
#       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
#     ],
#     "Accept-Encoding": [
#       "gzip, deflate, sdch"
#     ],
#     "Accept-Language": [
#       "en-US,en;q=0.8"
#     ],
#     "Cache-Control": [
#       "max-age=0"
#     ],
#     "CloudFront-Forwarded-Proto": [
#       "https"
#     ],
#     "CloudFront-Is-Desktop-Viewer": [
#       "true"
#     ],
#     "CloudFront-Is-Mobile-Viewer": [
#       "false"
#     ],
#     "CloudFront-Is-SmartTV-Viewer": [
#       "false"
#     ],
#     "CloudFront-Is-Tablet-Viewer": [
#       "false"
#     ],
#     "CloudFront-Viewer-Country": [
#       "US"
#     ],
#     "Host": [
#       "0123456789.execute-api.us-east-1.amazonaws.com"
#     ],
#     "Upgrade-Insecure-Requests": [
#       "1"
#     ],
#     "User-Agent": [
#       "Custom User Agent String"
#     ],
#     "Via": [
#       "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
#     ],
#     "X-Amz-Cf-Id": [
#       "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
#     ],
#     "X-Forwarded-For": [
#       "127.0.0.1, 127.0.0.2"
#     ],
#     "X-Forwarded-Port": [
#       "443"
#     ],
#     "X-Forwarded-Proto": [
#       "https"
#     ]
#   },
#   "requestContext": {
#     "accountId": "123456789012",
#     "resourceId": "123456",
#     "stage": "prod",
#     "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
#     "requestTime": "09/Apr/2015:12:34:56 +0000",
#     "requestTimeEpoch": 1428582896000,
#     "identity": {
#       "cognitoIdentityPoolId": None,
#       "accountId": None,
#       "cognitoIdentityId": None,
#       "caller": None,
#       "accessKey": None,
#       "sourceIp": "127.0.0.1",
#       "cognitoAuthenticationType": None,
#       "cognitoAuthenticationProvider": None,
#       "userArn": None,
#       "userAgent": "Custom User Agent String",
#       "user": None
#     },
#     "path": "/prod/path/to/resource",
#     "resourcePath": "/{proxy+}",
#     "httpMethod": "POST",
#     "apiId": "1234567890",
#     "protocol": "HTTP/1.1"
#   }
# }


# #print(
#     requests.post("http://localhost:9000/2015-03-31/functions/function/invocations", json=d, headers={"Content-Type":"application/json"}).text)


# '''
