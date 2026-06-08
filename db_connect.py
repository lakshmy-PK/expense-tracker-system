import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ammulakshmy22#",
    database="exp_tra"
)

cursor = conn.cursor()
print("connected successfully!")