
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

### How to Parse JSON String in Python 
Sometimes we are faced with data in JSON string format, and are confused about how to process it because it cannot be manipulated

Example of use :

```bash
json_string = '{"name":"ketsar","skillset":["programming","designing","testing"]}'
```

To convert JSON loads in string form to dictionary form, just use the Loads method or function from the Json module :
 
```bash
dict_data = json.loads(json_string)
```

### Parse Content in JSON File Into Dictionary 
The following is a way to read content data stored in a separate file for conversion to dictionary or JSON format:

- import json module
```bash
import json
```

- example of use: 
```bash
with open('%FOLDER DIRECTORY%\\%FILE_NAME%.txt') as f:
    read_json = json.load(f)

    print(read_json,'\n')
    print(type(read_json),'\n')
    
    print(read_json['KEY']['PROPERTY'],'\n')
    print(read_json['KEY']['PROPERTY'][INDEX],'\n')
    ...
```

### Parsing Complex JSON with Nested Structure and Extract Values 
To extract values from a very complex json code structure, searching manually is very troublesome, here is an example used to make the code look more concise :

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

- implementation in code :
```bash 
with open('%FOLDER DIRECTORY%\\%FILE_NAME%.txt') as f:
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


### Compare Two JSON Schemas
Sometimes we want to compare json data in one file with json data in another file, if there is even a slight difference it will be considered that the file has different data. the method is as follows:

```bash 
with open('%FOLDER DIRECTORY%\\%FILE_NAME%.txt') as f:
    read_json = json.load(f)
    assert read_json == read_json_1 # backend automation testing
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Deployment

To deploy this project run

```code
  npm run deploy
```


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

