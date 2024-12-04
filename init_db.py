import sqlite3


connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cursor = connection.cursor()

def create_mock_data():
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                   ("First Post", "Content for the first post"))
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                   ("Second Post", "Content for the second post"))
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                   ("Third Post", "Content for the third post"))

    connection.commit()
    connection.close()
