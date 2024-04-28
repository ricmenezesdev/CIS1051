from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

chromedriver_path = r'C:\Users\caput\AppData\Local\Programs\Python\Python312\chromedriver-win64\chromedriver.exe'
service = Service(chromedriver_path)
driver = Chrome(service=service)
driver.get("https://www.nytimes.com/games/wordle/index.html")


max_attempts = 6
attempts = 0
solved = False

while attempts < max_attempts:
    guess_word = generate_word()
    if not guess_word:
        break
   
    input_field = driver.find_element_by_css_selector('input[class^="InputField-pWVxY"]')
    input_field.clear()
    input_field.send_keys(guess_word)
    input_field.submit()
    
    time.sleep(60)
    
    correct_letters = driver.find_element_by_css_selector(".WordleSolution__feedback span:nth-child(2)").text
    correct_positions = driver.find_element_by_css_selector(".WordleSolution__feedback span:nth-child(1)").text
    print(f"Guess: {guess_word}, Correct Letters: {correct_letters}, Correct Positions: {correct_positions}")
    
    if correct_letters == "5":
        solved = True
        print("Wordle Solved!")
        break
    
    attempts += 1

if not solved:
    print("Wordle not solved. Better luck next time!")