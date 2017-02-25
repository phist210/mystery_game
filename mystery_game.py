import random
import sys
import os
import time
import re


def clean_sentence(sentence):
    return re.sub(r'[^A-Za-z]', '', sentence.lower())


def clear():
    os.system('clear')  # used to clear the screen for different sections


def pull_all_words():
    with open('/usr/share/dict/words', 'r') as dictionary:
        words = []

        for word in dictionary.readlines():
            words.append(word)
        return words


def pull_difficulty_level():
    level = input("\nEnter 1 for EASY, 2 for MEDIUM, any other key for HARD: ")

    if level == "1":
        return "easy"
    elif level == "2":
        return "medium"
    else:
        return "hard"


def pull_words_for_difficulty(words, difficulty):
    if difficulty == 'easy':  # numbers refer to word length
        return pull_words_min_max(words, 4, 6)
    elif difficulty == 'medium':
        return pull_words_min_max(words, 6, 8)
    else:
        return pull_words_min_max(words, 8, 99)


def pull_words_min_max(words, min_length, max_length):
    fixed_words = []  # pulls words depending on difficulty(word length)

    for word in words:
        if len(word) >= min_length and len(word) <= max_length:
            fixed_words.append(clean_sentence(word))
    return fixed_words


def pull_rand_word(fixed_words):  # chooses random word from fixed_words
    return fixed_words[random.randrange(0, len(fixed_words))]


def pull_guess(bad_guesses, good_guesses, mystery_word):
    while True:
        guess = input("Guess a letter: ").lower()
        board(bad_guesses, good_guesses, mystery_word)
        if guess == '':
            print("What was that?")
        elif len(guess) != 1:
            print("You can only guess a single letter!")

        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess LETTERS!")
        else:
            return guess


def board(bad_guesses, good_guesses, mystery_word):
    clear()

    print('** Strikes: {}/8 **'.format(len(bad_guesses)))
    print('')

    for guess in bad_guesses:  # displays bad guesses as a tally
        print(guess, end=" ")
    print('\n\n')

    for guess in mystery_word:
        if guess in good_guesses:
            print(guess, end=" ")
        else:
            print(' _ ', end=" ")  # displays blank spaces until a good guess

    print('')


def welcome():
    print('\n** Welcome to (no)Hangman!!! **\n')
    start = input("Press enter/return to start or Q to quit: ").lower()
    if start == 'q':
        print("See you next time!")
        sys.exit()
    else:
        return True


def play_again():
    play_again = input("\nPlay again? Y/n ").lower()
    if play_again != 'n':
        clear()
        welcome()
        main()
    else:
        print("\n\n\n\nCatch ya later!\n\n\n\n")
        time.sleep(1.5)
        clear()
        sys.exit()


def main():
    difficulty = pull_difficulty_level()
    words = pull_all_words()
    fixed_words = pull_words_for_difficulty(words, difficulty)
    mystery_word = pull_rand_word(fixed_words)
    bad_guesses = []
    good_guesses = []
    board(bad_guesses, good_guesses, mystery_word)
    done = False
    while not done:
        guess = pull_guess(bad_guesses, good_guesses, mystery_word)

        if guess in mystery_word:
            good_guesses.append(guess)
            found = True
            for guess in mystery_word:
                if guess not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}.".format(mystery_word))
                done = True
        elif guess not in mystery_word:
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                clear()
                print("\n **  ENGHH!  ** ")
                print("\nStrike ! You lost!")
                print("\nThe secret word was {}".format(mystery_word.upper()))
                done = True
        if done:
            play_again()

        else:
            board(bad_guesses, good_guesses, mystery_word)


if __name__ == '__main__':
    clear()
    welcome()
    main()
