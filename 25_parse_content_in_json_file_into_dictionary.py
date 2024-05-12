import json

with open('C:\\Users\\Devi\\Documents\\Document Ketsar\\PROJECT\\EXAMPLES\\json-data.txt') as f:
    read_json = json.load(f)

    print(read_json,'\n')
    print(type(read_json),'\n')
    
    print(read_json['project']['name'],'\n')
    print(read_json['project']['programming_languages'][0],'\n')
    print(read_json['project']['qa_test_cases'][1]['name'],'\n')
    print(read_json['project']['qa_test_cases'][1]['steps'][2],'\n')
    print(read_json['project']['qa_test_cases'][1]['expected_result'],'\n')
