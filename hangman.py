import random
from hangman_accessories import stages
from hangman_accessories import logo

def load_words(file):
    with open(file, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_random_word(words):

    return random.choice(words)

def guessed_word():
    letter = input("Guess a letter: ").lower()

    return letter


def blank_space(word_to_guess):
    display = []
    for i in range(len(word_to_guess)):
        display += "_"

    print(display)
    return display

def fill_in_the_blanks(word_to_guess,letter,display):
    for i in range(len(word_to_guess)):
        if letter == word_to_guess[i]:
            display[i] = letter

    print(display)
    return display


def game():
    print(logo)

    words = load_words('words_list.txt')
    word_to_guess = choose_random_word(words)
    blank_list = blank_space(word_to_guess)

    game_ended = False
    lives = 6
    list = []

    while not game_ended:
        guess = guessed_word()

        if guess in list:
            print(f"You've guessed '{guess}' already.")
        list.append(guess)


        filled_list = fill_in_the_blanks(word_to_guess, guess, blank_list)

        if '_' not in filled_list:
            game_ended = True
            print("Congratulations, you won!")


        if guess not in word_to_guess:
            print("wrong guess")
            lives = lives -1
            if lives == 0:
                game_ended = True
                print("Game Over!")


        print(stages[lives])
    print(f"the word you were supposed to guess was : {word_to_guess}")
    return filled_list


if __name__ == '__main__':
    game()
