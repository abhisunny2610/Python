import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="abhishek",
    password="abhishek123@"
)

if mydb.is_connected():
    print("Successfully Connected")
else:
    print("Connectivity Issue")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM test.test_table")

for i in mycursor.fetchall():
    print(i)

mydb.close()
