import requests
from utilities.configuration import *
from utilities.resources import *
from payload_method.payload_api import *

# ========================= ADD ==================================

config = getConfig()
url = getConfig()["API"]['endpoint'] + ApiResource.addBook
header = {'Content-Type': 'application/json'}
query = 'select * from Books'
addBook_response = requests.post(url, json=getPayloadFromDB(query), headers=header)
# addBook_response = requests.post(url, json=addBookPayload("a3a1"), headers=header)

if addBook_response.content != b'':
    print(addBook_response.json())
    print(type(addBook_response.json()))

    response_json = addBook_response.json()
    bookId = response_json['ID']
    print(bookId)

    # ========================= DELETE ==================================

    url = getConfig()['API']['endpoint'] + ApiResource.deleteBook
    header = {"Content-Type": "application/json"}

    delete_response = requests.post(url, json={"ID": bookId}, headers=header)
    assert delete_response.status_code == 200
    res_json = delete_response.json()
    print(res_json)
    print(res_json['msg'])
    assert res_json['msg'] == "book is successfully deleted"

else:
    print('addBook_response is empty')
