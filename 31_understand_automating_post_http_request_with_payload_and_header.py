import requests
from utilities.configuration import *
from utilities.resources import *
from payload_method.payload_api import *

# ========================= ADD ==================================

# standard code - optimized
'''
    [API]
    endpoint = http://216.10.245.166
'''

'''
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
'''

'''
    addBook = "/Library/Addbook.php"
    deleteBook = "/Library/DeleteBook.php"
'''

config = getConfig()
url = getConfig()["API"]['endpoint'] + ApiResource.addBook
header = {'Content-Type': 'application/json'}
response = requests.post(url, json=addBookPayload('aaabf'), headers=header)

print(response.json())
print(type(response.json()))

response_json = response.json()
bookId = response_json['ID']
print(bookId)

# ========================= DELETE ==================================

# response = requests.get("http://216.10.245.166/Library/GetBook.php",
#                         params={"AuthorName": "Ketsar Ali 2"})
#
# get_response = response.json()
# print(get_response)
#
# for get_data in get_response:
#     if get_data['isbn'] + get_data['aisle'] == 'aaa1239':
#         delete_data = {"ID": get_data['isbn'] + get_data['aisle']}
#         delete_response = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=delete_data)
#         print(delete_response.json())
#     else:
#         print({
#             "msg": "data doesn't exists"
#         })

url = getConfig()['API']['endpoint'] + ApiResource.deleteBook
header = {"Content-Type": "application/json"}

delete_response = requests.post(url, json={"ID": bookId}, headers=header)
assert delete_response.status_code == 200
res_json = delete_response.json()
print(res_json)
print(res_json['msg'])
assert res_json['msg'] == "book is successfully deleted"
