import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Insert image URLs into the table
images = [
    ('finance', '/static/finance.jpg'),
    ('energy', '/static/energy.jpg'),
    ('environment', '/static/environment.jpg')
]

cursor.executemany('INSERT INTO images (category, url) VALUES (?, ?)', images)

# Commit the changes and close the connection
conn.commit()
conn.close()
