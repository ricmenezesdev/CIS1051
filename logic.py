import random
import requests

url = "https://git.charlesreid1.com/cs/five-letter-words/raw/branch/master/sgb-words.txt"
response = requests.get(url)

def generate_word():
    if response.status_code == 200:
        words = response.text.split()
        random_word = random.choice(words)
        return random_word
    else:
        print("Failed to fetch the content. Status code:", response.status_code)

word = generate_word()
print(word)