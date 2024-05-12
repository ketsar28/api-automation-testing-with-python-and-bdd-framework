import json

json_string = '{"name":"ketsar","skillset":["programming","designing","testing"]}'

print(json_string)
print(type(json_string))

# loads method parse json string and it returns dictionary
dict_data = json.loads(json_string)

print(dict_data)
print(type(dict_data))

print(dict_data['name'])
print(type(dict_data['name']))

extract_skillset = dict_data['skillset']

extract_skillset.append('cooking')
extract_skillset.insert(1, 'playing')

print(extract_skillset)
print(type(extract_skillset))

print(extract_skillset[2])

