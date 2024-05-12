import json

with open('C:\\Users\\Devi\\Documents\\Document Ketsar\\PROJECT\\EXAMPLES\\json-data.txt') as f:
    read_json = json.load(f)

    # print(read_json,'\n')
    # print(type(read_json),'\n')
    
    # print(read_json['project']['name'],'\n')
    # print(read_json['project']['programming_languages'][0],'\n')
    # print(read_json['project']['qa_test_cases'][1]['name'],'\n')
    # print(read_json['project']['qa_test_cases'][1]['steps'][2],'\n')
    # print(read_json['project']['qa_test_cases'][1]['expected_result'],'\n')

    # print(f'{10 * '='} Next {10 * '='}')

    # print(type(read_json['project']['qa_test_cases']),'\n')

    # for qa_test_case_data in read_json['project']['qa_test_cases']:

    #     if qa_test_case_data['name'] in "add new user functionality".capitalize():

    #         for steps_test_case_data in qa_test_case_data['steps']:
    #             print(steps_test_case_data)

    #             if steps_test_case_data in "verify new user is listed in the user table".capitalize():
    #                 print('\n')
    #                 print(steps_test_case_data)

    #                 assert steps_test_case_data in "verify new user is listed in the user table".capitalize()
            
    print(f'{10 * '='} Next {10 * '='}')

with open('C:\\Users\\Devi\\Documents\\Document Ketsar\\PROJECT\\EXAMPLES\\json-data-1.txt') as f1:
    read_json_1 = json.load(f1)
    # print(read_json == read_json_1)
    assert read_json == read_json_1 # backend automation testing

