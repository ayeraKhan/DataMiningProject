import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('images.db')
cursor = conn.cursor()

# Create a table to store image information
cursor.execute('''CREATE TABLE IF NOT EXISTS Images
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, filepath TEXT)''')

# Function to insert image information into the database
def insert_image(filename, filepath):
    cursor.execute("INSERT INTO Images (filename, filepath) VALUES (?, ?)", (filename, filepath))
    conn.commit()

# Function to retrieve image information from the database
def get_image(image_id):
    cursor.execute("SELECT filename, filepath FROM Images WHERE id=?", (image_id,))
    result = cursor.fetchone()
    if result:
        return result[0], result[1]
    else:
        return None

# Example usage
insert_image("finance_smooting.PNG", "finance_smoothing.PNG")

image_id = 1
filename, filepath = get_image(image_id)
if filepath:
    print("finance_smooting.PNG", filename)
    print("finance_smoothing.PNG", filepath)
else:
    print("Image not found.")
