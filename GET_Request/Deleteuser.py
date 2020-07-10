import requests
import jsonpath


def deleteuser():
    url = 'https://reqres.in/api/users/2'
    response = requests.delete(url)

    # fetch response code
    print(response.status_code)
    assert response.status_code == 204


print('This is Deleteuser function')
