from utilities.configuration import *


def addBookPayload(isbn):
    data = {'name': "Python JS Java 10", 'isbn': isbn, 'aisle': 12310, 'author': "Ketsar Ali 2"}
    return data


def addBookPayload2(isbn, aisle):
    data = {
        'name': "Python JS Java 10",
        'isbn': isbn,
        'aisle': aisle,
        'author': "Ketsar Ali 2"}
    return data


def getPayloadFromDB(query):
    data = {}
    result = getQuery(query)
    data['name'] = result[0]
    data['isbn'] = result[1]
    data['aisle'] = result[2]
    data['author'] = result[3]
    print(data)
    print(type(data))
    return data
