import json
import jsonpath
import requests


    # adding technical details
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('C:/Users/APIAutomation/GET_Request/postjson.json', 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id([0]))
    request_json['st_id'] = int(id([0]))
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    # adding address
    add_api_url = "http://thetestingworldapi.com/api/addresses"
    file = open('C:/Users/APIAutomation/GET_Request/postaddressjson.json', 'r')
    request_json = json.loads(file.read())
    request_json['stId'] = str(id([0]))
    response = requests.post(add_api_url, request_json)
    print(response.text)
    print(response.status_code)
    print('Address added successfully')

    # fetch complete details of the student
    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id([0]))
    response = requests.get(final_details)
    print(response.text)
