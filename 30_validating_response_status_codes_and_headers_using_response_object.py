import requests
import json

response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params={"AuthorName": "Ketsar Ali 2"})

# print(response.text)
# print(type(response.text))
#
# list_response = json.loads(response.text)
# print(list_response)
# print(type(list_response))
#
# get_isbn = list_response[0]['isbn']
# print(get_isbn)
#
list_response_2 = response.json()
# get_isbn_2 = list_response_2[0]['isbn']
# print(get_isbn_2)

print("status code is =", response.status_code)
assert response.status_code == 200

# print(response.headers)
# print(response.headers['Content-Type'])
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

print(f'{10 * "="}')
# retrieve the book details with ISBN aaa1232
for actualBook in list_response_2:
    # print(actualBook['isbn'] + actualBook['aisle'])
    if actualBook['isbn'] + actualBook['aisle'] in 'aaa1237':
        print(actualBook)
        break

expectedBook = {
    'book_name': 'Python JS Java 7',
    'isbn': 'aaa',
    'aisle': '1237'
}

assert actualBook == expectedBook
