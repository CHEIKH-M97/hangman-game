from colorama import Fore , Style , init
import os
import emoji
import inquirer
import random
import ctypes
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  X   |
      |
      |
      |
      |
=========''',]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW('Hangman Game - CHEIKH M97')
os.system(f'mode con: cols={100} lines={20}')
y=10*'  '
def back_to_main_menu():
    question = [inquirer.List('choice',message='BACK TO MAIN MENU ',choices=["[>] YES","[>] NO , QUIT"])]
    res = inquirer.prompt(question)
    return 'YES' in res['choice']
def get_choiceandtheme():
    choice = [
        inquirer.List(
            'choice',
            message ="Choose the game mode : Use up/down arrow to scroll and Enter to confirm".center(100),
            choices=[
                     "[>] 3-letter word",
                     "[>] 4-letter word",
                     "[>] 5-letter word", 
                     "[>] 6-letter word",
                     "[>] Help", 
                     "[>] Quit",])]
    theme = [
        inquirer.List('theme',
            message = "Choose the game theme : Use up/down arrow to scroll and Enter to confirm".center(100),
            choices=[emoji.emojize(':red_question_mark:  Random'),
                     emoji.emojize(':police_car:  Cars'),
                     emoji.emojize(':triangular_flag: Countries'),
                     emoji.emojize(':dog:  Animals')])]
    choice = inquirer.prompt(choice)
    if 'Help' in choice['choice']:
        _help()
        return None , None
    elif "Quit" in choice['choice']:
        quit
    else:
        theme = inquirer.prompt(theme)
        return choice['choice'] , theme['theme']
t1 = {

    3: ["cat", "dog", "bat", "fox", "ant", "rat"],
    4: ["wolf", "lion", "bear", "crow", "crab", "frog", "dove"],
    5: ["horse", "gecko", "panda", "shark", "fishy", "hound"],
    6: ["rabbit", "donkey", "parrot", "ferret", "pigeon", "weasel"],
}
t2 = {
    3: ["cat", "dog", "sun", "bat", "hat", "car"],
    4: ["tree", "frog", "desk", "ship", "lion", "duck"],
    5: ["apple", "grape", "chair", "stone", "brush"],
    6: ["banana", "cherry", "guitar", "planet", "bridge"],
}
t3 = {
    3: ["USA", "UAE", "TUN", "GER", "Cay"], 
    4: ["Iraq", "Iran", "Cuba", "mali", "Chad", "Peru", "Oman"],  
    5: ["Chile", "Japan", "Kenya", "Ghana", "China","india","nepal",'italy'], 
    6: ["Brazil", "Canada", "France", "Greece","jordan","angola","mexico"], 
}
t4 = {
    3: ["BMW", "GMC", "RAM", "Kia"], 
    4: ["Audi", "Honda", 'Mini', "Fiat", "TATA",  "JEEP", "Ford", 'Seat','Opel'],  
    5: ["Tesla", "volvo", "Honda", "mazda","Dodge"], 
    6: ["Jaguar", "Peugot", "passat", "Toyota", 'Nissan'],  
}
def get_valid_guess():
    while True:
        guess = input(Fore.MAGENTA + y+"Guess a Letter ! --> ")
        if not 'A'<=str(guess).upper()<='Z':
            print(Fore.RED + 'Invalid input ! Try again.')
        else: 
            return guess.upper()
def _help():
    print('this section is not implemented yet')
def print_centered(x):
    lines = x.splitlines()
    for line in lines:
        print(y+line)
def play_game(x,theme):
    t=0
    clear_screen()
    for char in x:
        if char.isdigit():
            t+=int(char)
    if 'Random' in theme:
        word = random.choice(t2[t]).upper()
    elif 'Countries' in theme:
        word = random.choice(t3[t]).upper()
    elif  'Cars' in theme:
        word = random.choice(t4[t]).upper()
    if  'Animals' in theme:
        word = random.choice(t1[t]).upper()
    check = word
    guess_word = t * '_'
    hang = 0
    lives = 6
    while guess_word != word and hang < 6:
        print(13*'  '+guess_word)
        print_centered(hangman[hang])
        guess = get_valid_guess()
        i = check.find(guess)
        if i != -1:
            guess_word = guess_word[:i] + guess + guess_word[i+1:]
            check = check[:i] + '*' + check[i+1:]
            print(y+Fore.GREEN + f"True ! The Letter {guess} exists.   Lives remaning = {lives}")
        else:
            lives -= 1
            hang += 1
            print(y+Fore.RED +f"Invalid Letter.    Lives remaining = {lives}")
    if guess_word == word:
        print(y+Fore.GREEN + 'YOU WON')
    elif hang ==6:
        print_centered(hangman[6])
        print(y+Fore.RED + 'YOU LOST') 
    print(y+Fore.MAGENTA +Style.BRIGHT +  f"The word is : {word}")
def main():
    while True:
        clear_screen()
        choice , theme = get_choiceandtheme()
        if choice == None:
            if not back_to_main_menu():
                return
            continue
        play_game(choice,theme)
        if not back_to_main_menu():
            return
if __name__ == '__main__':
    main()