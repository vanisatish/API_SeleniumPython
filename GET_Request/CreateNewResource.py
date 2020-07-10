import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'
# read input json file
file = open('C:/Users/APIAutomation/CreatejsonUser.json', 'r')
json_input = file.read()
# parse or typecast data into json format as the default format is string
request_json = json.loads(json_input)
print(request_json)

# make POST request with JSON input body
response = requests.post(url, request_json)
print(response.content)

# validating response code
assert response.status_code == 201

# fetch header from response
print(response.headers)

# fetch specific header
print(response.headers.get('Content-Length'))

# parse response to JSON format 'id' is numeric- loads() is for turning JSON encoded data into Python objects
response_json = json.loads(response.text)

# pick id using json path
extract_id = jsonpath.jsonpath(response_json, 'id')

# fetch first id
print(extract_id[0])

