import json
import jsonpath
import requests


def test_Add_new_data():
    # adding a student
    # app_url = "http://thetestingworldapi.com/api/studentsDetails"
    # file = open('C:/Users/satis/AppData/Local/Programs/Python/Python37-32/APIAutomation/GET_Request/Requestjson.json', 'r')
    # request_json = json.loads(file.read())
    # response = requests.post(app_url, request_json)
    # print(response.text)
    # id = jsonpath.jsonpath(response.json(), 'id')
    # print(id[0])


    # adding technical details
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('C:/Users/satis/AppData/Local/Programs/Python/Python37-32/APIAutomation/GET_Request/postjson.json', 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id([0]))
    request_json['st_id'] = int(id([0]))
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    # adding address
    add_api_url = "http://thetestingworldapi.com/api/addresses"
    file = open('C:/Users/satis/AppData/Local/Programs/Python/Python37-32/APIAutomation/GET_Request/postaddressjson.json', 'r')
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