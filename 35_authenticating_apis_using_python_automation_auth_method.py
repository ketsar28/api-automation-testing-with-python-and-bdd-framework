import requests
from requests import auth

from utilities.configuration import *

# Authentication - GitHub
url = "https://api.github.com/users"
github_response = requests.get(url,verify=False, auth=('ketsar28',getPassword()))

print(github_response.text)
print(type(github_response.text))
print(github_response.status_code)