
import random
import requests


url = "https://git.charlesreid1.com/cs/five-letter-words/raw/branch/master/sgb-words.txt"

response = requests.get(url)

def generateWord():
    if response.status_code == 200:
        words = response.text.split()
        random_word = random.choice(words)
        print(random_word)
    else:
        print("Failed to fetch the content. Status code:", response.status_code)

generateWord()
   
'''
def checkGuess(target_word, guess):
    feedback = {'green': 0, 'yellow': 0, 'gray': 0}
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            feedback['green'] += 1
        elif guess[i] in target_word:
            feedback['yellow'] += 1
        else:
            feedback['gray'] += 1
    return feedback

# Example usage:
target_word = generateWord()
print("Target Word:", target_word)

user_guess = input("Enter your guess: ")
feedback = checkGuess(target_word, user_guess)
print("Feedback:", feedback)

'''