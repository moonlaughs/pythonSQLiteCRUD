import sqlite3
import uuid

# Database
db = sqlite3.connect('data.db')

id = str(uuid.uuid4())
name = "ABC"

#Insert data
db.execute('INSERT INTO users VALUES(?,?)', (id, name))
db.commit() # save the data