from email.policy import HTTP

import requests


# endpoint = "https://httpbin.org/status/200/"

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint)      # HTTP request
# get_response_with_json = requests.get(endpoint, json={"query":"Hello World"})
# get_response_with_data = requests.get(endpoint, data={"query":"Hello World"})
# print(get_response.text)        # print raw text response with https://httpbin.org and json with https://httpbin.org/anything
# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# print(get_response.json())      # prints python Dictionary
# print(get_response_with_json.json())
# print(get_response_with_data.json())
get_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World from client"})
# get_response = requests.get(endpoint, params={"abc": 123})

# print(get_response.encoding)
# print(get_response.status_code)
# print(get_response.json()['message'])
print(get_response.json())
