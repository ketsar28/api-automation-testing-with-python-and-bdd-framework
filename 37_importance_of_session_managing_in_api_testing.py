import requests
from utilities.configuration import *

# Authentication - GitHub

session = requests.session()
session.auth = auth=("ketsar28",getPassword())

url = "https://api.github.com/user"
github_response = requests.get(url,verify=False, auth=("ketsar28",getPassword()))

print(github_response.text)
print(type(github_response.text))
print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
# list_repos_github_response = requests.get(url2, auth=("softwaredev28",getPassword()))
list_repos_github_response = session.get(url2)
print(list_repos_github_response.text)
