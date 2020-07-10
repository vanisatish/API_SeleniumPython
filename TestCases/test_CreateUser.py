import requests
import json
import jsonpath

# Create TestCases directory and python file name should either begin or have test in the file name
url = 'https://reqres.in/api/users'


# run the tests at command prompt like so:  "pytest -v -s TestCases" this will execute all methods under that directory

def test_create_new_user():
    # read input json file
    file = open('C:/Users/satis/AppData/Local/Programs/Python/Python37-32/APIAutomation/CreatejsonUser.json', 'r')
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


# calling multiple test cases in one file
def test_create_other_user():
    file = open('C:/Users/satis/AppData/Local/Programs/Python/Python37-32/APIAutomation/GET_Request/updateResource.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    # make PUT request
    response = requests.put(url, request_json)
    assert response.status_code == 200

    # parse response content or validate response content. Extract value of 'updatedAt'
    response_json = json.loads(response.text)
    updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
    print(updated_li)
