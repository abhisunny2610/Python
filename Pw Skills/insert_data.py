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
mycursor.execute("INSERT INTO test.test_table values(5034, 'Abhishek Singh', 'Data Science', 853280)")
mydb.commit()
mydb.close()