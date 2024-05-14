import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table to store image URLs
cursor.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,
    url TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
