import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="game_db"
)

if (db.is_connected) :
    print('berhasil terhubung')


cursor = db.cursor()

# create table enemy

cursor.execute(
    "CREATE TABLE IF NOT EXISTS hero (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), health INT, damage INT)"
)

cursor.execute(
    "CREATE TABLE IF NOT EXISTS enemy (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), health INT, damage INT)"
)