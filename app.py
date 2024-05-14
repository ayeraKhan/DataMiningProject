from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def fetch_image_url(category):
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM images WHERE category = ? LIMIT 1", (category,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image', methods=['POST'])
def get_image():
    dataset = request.form['option']
    model = request.form['model']
    # You can process the dataset and model as needed here
    image_url = fetch_image_url(dataset)
    if image_url:
        return jsonify({'url': image_url, 'model': model})
    else:
        return jsonify({'error': 'Image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
