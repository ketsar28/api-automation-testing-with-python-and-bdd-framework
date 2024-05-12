import os

import requests
from behave import *
from utilities.configuration import *
from utilities.resources import *
from payload_method.payload_api import *


# BOOK API

@given('the Book details which needs to be added to library')
def step_impl(context):
    context.url = getConfig()["API"]['endpoint'] + ApiResource.addBook
    context.header = {'Content-Type': 'application/json'}
    context.payload = addBookPayload("joss")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.header)


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json['Msg'] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()["API"]['endpoint'] + ApiResource.addBook
    context.header = {'Content-Type': 'application/json'}
    context.payload = addBookPayload2(isbn, aisle)


# GITHUB API

@given(u'I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('ketsar28', getPatFromEnv())


@when(u'I Hit gitRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResource.gitHub)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

#
# @given('I am authenticated to GitHub')
# def set_authentication(context):
#     context.session = requests.session()
#     context.session.auth = ('ketsar28', getPatFromEnv())
#
#
# @when('I get user information')
# def get_user_info(context):
#     url = "https://api.github.com/user"
#     context.response = context.session.get(url, verify=False)
#     context.user_info = context.response.json()  # Store response data in context
#
#
#
# @then('the response status code should be {expected_status_code}')
# def verify_status_code(context, expected_status_code):
#     print(int(expected_status_code))
#     assert context.response.status_code == int(expected_status_code)
#
#
# @then(u'the response body should contain the user\'s data')
# def step_impl(context):
#     print(context.user_info)
