import mysql.connector as db

# host, database name, username, password

connect_db = db.connect(host="localhost",database="PythonAutomation",username="root",password="password")
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
for row in multiple_rows:
    print(f'{idx} - {row}')
    idx += 1

