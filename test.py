import mysql.connector

MyDB = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="bot")

cursor = MyDB.cursor('bot')
cursor.execute("SELECT")