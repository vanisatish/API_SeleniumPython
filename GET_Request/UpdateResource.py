import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users/2'

# read data from json file
file = open('C:/Users/satis/APIAutomation/updateResource.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# make PUT request
response = requests.put(url, request_json)
assert response.status_code == 200

# parse response content or validate response content. Extract value of 'updatedAt'
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li)
