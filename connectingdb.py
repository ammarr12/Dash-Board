import mysql.connector

mydb = mysql.connector.connect(
    
    host = "127.0.0.1",
    user = "root",
    password = "qwerty1234"
)

cursor=mydb.cursor()
cursor.execute("Use Dashboard")
cursor.execute("Select * from HospitalDataAnalysis")