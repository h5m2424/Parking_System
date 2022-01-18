import mysql.connector

pk_db = mysql.connector.connect(
    host="192.168.1.15",
    user="pk",
    passwd="1234"
)

print(pk_db)

