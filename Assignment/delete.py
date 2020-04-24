import sqlite3

db = sqlite3.connect('data.db')

db.execute('DELETE FROM users WHERE id = ?', ('5a85126e-667d-433a-bad9-40b926d93dac',))
db.commit()