import requests

from utilities.configuration import *
from utilities.resources import *

session = requests.session()
session.auth = ('ketsar28', getPatFromEnv())

response = session.get(ApiResource.gitHub, verify=False)
user_info = response.json()  # Store response data in context
print(user_info)
print(response.status_code)
