# import mysql.connector as db
from utilities.configuration import *

# host, database name, username, password
# connect_db = db.connect(host="localhost", database="APIDevelop", username="root", password="password")
# print(connect_db.is_connected())

connection = getConnection()
cursor = connection.cursor()

cursor.execute("select * from CustomerInfo")

single_row = cursor.fetchone()
print(single_row)
print(single_row[1:3])
print(type(single_row))

single_row = cursor.fetchone()

multiple_rows = cursor.fetchall()
idx = 0
sum = 0
for row in multiple_rows:
    sum += row[2]
    print(f'{idx} - temporary result = {sum}')
    idx += 1

print(f'result sum =', sum)

# update data
query_update = "update CustomerInfo set location = %s where courseName = %s;"
arguments = ('indonesia','Appium')
cursor.execute(query_update,arguments)

# insert data
query_insert = "insert  CustomerInfo where courseName ="

connection.commit()
connection.close()
