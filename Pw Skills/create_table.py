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
mycursor.execute(
    "CREATE TABLE if not exists test.test_table(c1 INT, c2 VARCHAR(30), c3 VARCHAR(30), c4 INT)")
mydb.close()
