from flask import Flask
from flask_cors import CORS
from flask import jsonify
import random
import requests

app = Flask(__name__)
CORS(app)

@app.route('/word')
def generate_word():
    url = r"https://git.charlesreid1.com/cs/five-letter-words/raw/branch/master/sgb-words.txt"

    response = requests.get(url)
    if response.status_code == 200:
        words = response.text.split()
        word = random.choice(words)
        return jsonify({'word': word})
    else:
        print("Failed to fetch the content. Status code:", response.status_code)
        return jsonify({'error': 'Failed to fetch the content'}), 500
    
@app.route('/')
def home():
    word = generate_word()
    return word

if __name__ == '__main__':
    app.run(debug=True)
