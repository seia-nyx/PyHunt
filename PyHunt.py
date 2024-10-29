import random

easy_words = ('apple', 'orange', 'banana', 'plate', 'fair', 'ring', 'monkey', 'music', 'ballpen', 'perfume', 'center', 'case', 'paper')
hard_words = ('algorithm', 'dashboard', 'encryption', 'gigabyte', 'calligraphy', 'anthropology', 'astronomy')


hangman_art = {0: ("     ",
                    "     ",
                    "     "),
               1: ("  o  ",
                   "     ",
                   "   "),
               2: ("  o  ",
                   "  |  ",
                   "     "),
               3: ("  o  ",
                   " /|  ",
                   "     "),
               4: ("  o  ",
                   " /|\\ ",
                   "     "),
               5: ("  o  ",
                   " /|\\ ",
                   " /   "),
               6: ("  o  ",
                   " /|\\ ",
                   " / \\ ")}

def main():
    print('''Welcome to PyHunt!
You are given 1 hint, to use this simply type 'hint'.''')

    while True:
        difficulty = input("Choose a difficulty (easy/hard): ").lower()

        if difficulty == "easy":
            play_game(easy_words)
        elif difficulty == "hard":
            play_game(hard_words)
        else:
            print("Invalid difficulty choice. Please try again.")
            continue

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break
          

def display_man(wrong_guesses):
    print("-----")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-----")

def display_hint(hint):
    print(" ".join(hint))

def reveal_letter(hint, answer, lives):
    revealed_letters = set(hint)
    unrevealed_letters = set(answer) - revealed_letters
    if unrevealed_letters:
        random_letter = random.choice(list(unrevealed_letters))
        for i in range(len(answer)):
            if answer[i] == random_letter:
                hint[i] = random_letter
        lives -= 1
        print(f"You revealed the letter '{random_letter}'.")
    else:
        print("All letters have already been revealed.")
    return hint, lives

def play_game(words):
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    lives = 1
    hint_used = False  
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if guess == "hint":
            if not hint_used:  
                hint, lives = reveal_letter(hint, answer, lives)
                wrong_guesses += 1
                hint_used = True  
            else:
                print("No hints left.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            if all(letter != "_" for letter in hint):
                print("You Win!")
                is_running = False
                
        else:
            wrong_guesses += 1
            if wrong_guesses == len(hangman_art):
                print("Game Over! The word was:", answer)
                is_running = False
        


main()