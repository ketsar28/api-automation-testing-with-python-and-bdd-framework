
# API Automation Testing with Python & BDD Framework

Build Python automation Utilities to test Rest API’s with SQL DB Integration, Batch Jobs Automation,Web Scraping etc


## Section

 - Read and Write to JSON Files and Parsing using Python Methods
 - API Automation Testing with Python Requests Library
 - Setting up Global Properties and OAuth Mechanism for API Testing
 - API Testing Request Library Miscellaneous Concepts
 - Build SQL Utility to Interect with Database Tables from Python Code
 - Integrate Database Utilities to API Test for End to Automation
 - BDD Framework Development for API Automation
##  Read and Write to JSON Files and Parsing using Python Methods

### 1. How to Parse JSON String in Python 
Sometimes we are faced with data in JSON string format, and are confused about how to process it because it cannot be manipulated

Example of use:

```bash
json_string = '{"name":"ketsar","skillset":["programming","designing","testing"]}'
```

To convert JSON loads in string form to dictionary form, just use the Loads method or function from the Json module:
 
```bash
dict_data = json.loads(json_string)
```

### 2. Parse Content in JSON File Into Dictionary 
The following is a way to read content data stored in a separate file for conversion to dictionary or JSON format:

- import json module
```bash
import json
```

- example of use: 
```bash
with open('%FOLDER_DIRECTORY%\\%FILE_NAME%.txt') as f:
    read_json = json.load(f)

    print(read_json,'\n')
    print(type(read_json),'\n')
    
    print(read_json['KEY']['PROPERTY'],'\n')
    print(read_json['KEY']['PROPERTY'][INDEX],'\n')
    ...
```

### 3. Parsing Complex JSON with Nested Structure and Extract Values 
To extract values from a very complex json code structure, searching manually is very troublesome, here is an example used to make the code look more concise:

- example of json data used
```bash
{
  "project": {
    "name": "Belajar Coding",
    "programming_languages": [
      "Python",
      "JavaScript"
    ],
    "qa_test_cases": [
	 
      {
        "name": "Search functionality",
        "steps": [
          "Open application search bar",
          "Enter search term",
          "Click search button",
          "Verify search results are displayed"
        ],
        "expected_result": "Relevant search results are displayed based on the search term"
      },
	  {
        "name": "Login functionality",
        "steps": [
          "Open application login page",
          "Enter valid username and password",
          "Click login button",
          "Verify successful login message is displayed"
        ],
        "expected_result": "User is redirected to the home page"
      },     
	 {
        "name": "Add new user functionality",
        "steps": [
          "Navigate to user management page",
          "Click 'Add New User' button",
          "Enter user details (name, email, password)",
          "Click 'Save' button",
          "Verify new user is listed in the user table"
        ],
        "expected_result": "New user is successfully created and added to the user table"
      },
      {
        "name": "Edit user profile functionality",
        "steps": [
          "Navigate to user management page",
          "Select a user from the user table",
          "Click 'Edit User' button",
          "Modify user details (name, email)",
          "Click 'Save Changes' button",
          "Verify user details are updated in the user table"
        ],
        "expected_result": "User details are successfully updated in the user table"
      }
    ]
  }
}
```

- implementation in code:
```bash 
with open('%FOLDER_DIRECTORY%\\%FILE_NAME%.txt') as f:
    read_json = json.load(f)

     print(type(read_json['project']['qa_test_cases']),'\n')

    for qa_test_case_data in read_json['project']['qa_test_cases']:

        if qa_test_case_data['name'] in "add new user functionality".capitalize():

            for steps_test_case_data in qa_test_case_data['steps']:
                print(steps_test_case_data)

                if steps_test_case_data in "verify new user is listed in the user table".capitalize():
                    print('\n')
                    print(steps_test_case_data)

                    assert steps_test_case_data in "verify new user is listed in the user table".capitalize()
            
```

### 4. Compare Two JSON Schemas
- Sometimes we want to compare json data in one file with json data in another file, if there is even a slight difference it will be considered that the file has different data. the method is as follows:

```bash 
with open('%FOLDER_DIRECTORY%\\%FILE_NAME%.txt') as f:
    read_json = json.load(f)
    assert read_json == read_json_1 # backend automation testing
```


## API Automation Testing with Python Requests Library

### 1. Understanding Get HTTP Request Calls And Get Response Using JSON Methods
To make an http request call, a library or module is needed that needs to be imported, including:
- requests
- json

Because [`requests`](https://pypi.org/project/requests/) is an external library, we need to install it so it can be used in the project:
```
pip install requests
```

import it into the python file used:
```
import requests
import json
```

In the requests library there are many methods provided to implement calling http requests using the following examples:
```
response = requests.get("%BASE_URL%/%RESOURCE%",
                        params={"PROPERTY": "VALUE"})

print(response.text)
print(type(response.text))
```

to convert the type of data that has been obtained after making an http call by using the  [`load()`](https://www.geeksforgeeks.org/json-loads-in-python/) function :
```
list_response = json.loads(response.text)
print(list_response)
print(type(list_response))
```
After being converted using the loads() method to a list or dictionary, the response data can be manipulated

### 2. Validating [`Response Status Code`](https://www.geeksforgeeks.org/response-status_code-python-requests/) and [`Headers`](https://blog.postman.com/what-are-http-headers/)
- Sometimes when we do a test, we want to compare the expected value with the value obtained. In Python there are statements that can be used to do this by utilizing the [`assert`](https://www.upgrad.com/tutorials/software-engineering/python-tutorial/assert-keyword-in-python/#:~:text=Python's%20%22assert%22%20keyword%20validates%20code,True%2C%20the%20program%20runs%20uninterrupted.) statement, here is an example:
```
response = requests.get("%BASE_URL%/%RESOURCE%", params={"PROPERTY": "VALUE"})

assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
```
- other examples could also be like this:
```
json_response = response.json()

for actualBook in json_response:
    if actualBook['isbn'] + actualBook['aisle'] in 'aaa1237':
        print(actualBook)
        break

expectedBook = {
    'book_name': 'Python JS Java 7',
    'isbn': 'aaa',
    'aisle': '1237'
}

assert actualBook == expectedBook
```

### 3. Understand Automating [`POST HTTP Request`](https://en.wikipedia.org/wiki/POST_(HTTP)) With [`Payload`](https://blog.hubspot.com/website/what-is-payload) and Headers

- To send data to the backend server of an application, you can use the [`post()`](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests) method from the requests library by sending several necessary parameters
```
url = BASE_URL + RESOURCE
header = {'Content-Type': 'application/json'}
post_response = requests.post(url, json={'KEY': 'VALUE'}, headers=header)
```
prints the results to the console or terminal: 
```
print(post_response.json())
print(type(post_response.json()))
```
- and in this example case, to delete data that has been stored on the server, you can use the [`post()`](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests) method as well
```
response_json = post_response.json()
bookId = response_json['ID']

delete_response = requests.post(url, json={"ID": bookId}, headers=header)
```
carry out debugging or check whether the results obtained match the expected results
```
assert delete_response.status_code == 200
res_json = delete_response.json()
assert res_json['msg'] == "book is successfully deleted"
```

So that the code is compiled more optimally, we can separate certain codes into different files :
- To make an http request call, you need to send a URL including the base URL and the resource path. To accommodate the base URL, it would be better to separate it from the resource storage, and the best way is to store the base URL in a file with the extension .ini (for example: properties.ini), which contains the following code:
  ```
  [API] # section
  endpoint = PROTOCOL://%DOMAIN%
  ```

- create a file (resources) containing class code with any name (for example: ApiResource), this class functions to hold resources that will be used at a certain base url to make http request calls
  ```
  class ApiResource:
    addBook = "/Library/Addbook.php"
    deleteBook = "/Library/DeleteBook.php"
    gitHub = "https://api.github.com/user/repos"
  ```
- then, create a separate python file (payload_api) to accommodate the payload that will be sent when calling the http request. for example as follows
  ```
  def addBookPayload(isbn):
    data = {'name': "Python JS Java 10", 'isbn': isbn, 'aisle': 12310, 'author': "Ketsar Ali 2"}
    return data
  ```
- To get the base URL from a file with the .ini extension, an additional module is required to be imported into the file to be used, as follows
  ```
  pip install configparser
  ```
  ```
  import configparser
  ```
  ```
  def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
  ```
