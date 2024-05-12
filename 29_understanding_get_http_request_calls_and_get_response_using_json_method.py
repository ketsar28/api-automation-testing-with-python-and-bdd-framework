import requests
import json

response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params={"AuthorName": "John foe 1"})

print(response.text)
print(type(response.text))

list_response = json.loads(response.text)
print(list_response)
print(type(list_response))

get_isbn = list_response[0]['isbn']
print(get_isbn)

list_response_2 = response.json()
get_isbn_2 = list_response_2[0]['isbn']
print(get_isbn_2)
