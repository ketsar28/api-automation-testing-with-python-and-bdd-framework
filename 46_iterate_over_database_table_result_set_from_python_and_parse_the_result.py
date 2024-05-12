import mysql.connector as db

# host, database name, username, password

connect_db = db.connect(host="localhost", database="APIDevelop", username="root", password="password")
# print(connect_db.is_connected())
query = connect_db.cursor()

query.execute("select * from CustomerInfo")

single_row = query.fetchone()
print(single_row)
print(single_row[1:3])
print(type(single_row))

single_row = query.fetchone()

multiple_rows = query.fetchall()
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
query.execute(query_update,arguments)

connect_db.commit()
connect_db.close()
