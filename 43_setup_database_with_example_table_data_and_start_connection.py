import mysql.connector as db

# host, database name, username, password

connect_db = db.connect(host="localhost",database="PythonAutomation",user="root",password="password")
print(connect_db.is_connected())