import requests
from utilities.configuration import *
from utilities.resources import *


def  after_scenario(context, scenario) :
    if "booklibrary" in scenario.tags:
        url = getConfig()['API']['endpoint'] + ApiResource.deleteBook
        header = {"Content-Type": "application/json"}

        delete_response = requests.post(url, json={"ID": context.bookId}, headers=header)
        assert delete_response.status_code == 200
        res_json = delete_response.json()
        print(res_json)
        print(res_json['msg'])
        assert res_json['msg'] == "book is successfully deleted"