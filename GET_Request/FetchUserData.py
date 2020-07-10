import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"  # API URL

# Send GET request
response = requests.get(url)
print(response)

# display response content
print(response.content)
print(response.json())
print(response.headers)

# another way to print response data using json methods
json_response = json.loads(response.text)
print(json_response)

# fetch specific value from the response by using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])   # print pages of index 1 i.e. first value of total pages
# fetch first value of the json value
assert pages[0] == 2
