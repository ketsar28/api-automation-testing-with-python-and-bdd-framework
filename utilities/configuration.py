import configparser
import mysql.connector as db
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPatFromEnv():
    return getConfig()['PAT']['token']


connect_db = {
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password']
}


def getPassword():
    return "telkomsel2005"


def getConnection():
    try:
        conn = db.connect(**connect_db)
        if conn.is_connected():
            print("connection successfully")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result
