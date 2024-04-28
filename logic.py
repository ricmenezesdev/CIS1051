import random
import requests
import time


def generate_word():
    url = r"https://git.charlesreid1.com/cs/five-letter-words/raw/branch/master/sgb-words.txt"

    response = requests.get(url)
    if response.status_code == 200:
        words = response.text.split()
        random_word = random.choice(words)
        return random_word
    else:
        print("Failed to fetch the content. Status code:", response.status_code)
        return None
wrd = generate_word()
print(wrd)