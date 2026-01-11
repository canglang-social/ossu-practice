# Problem Set 2, hangman.py
# Name: FelixOrion
# Collaborators:
# Time spent: 251209 Dinner SelfReview

import random
import string
import os

# -----------------------------------
# HELPER CODE
# -----------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORDLIST_FILENAME = os.path.join(SCRIPT_DIR, "words.txt")


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = True
    for i in secret_word:
        if i not in letters_guessed:
            result = False
    return result


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for i in secret_word:
        if i in letters_guessed:
            result += i
        else:
            result += "*"
    return result


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            result += i
    return result


def input_is_legal(user_input, with_help):
    if with_help:
        return len(user_input) == 1 and (user_input.isalpha() or user_input == "!")
    else:
        return len(user_input) == 1 and user_input.isalpha()


def increase_guess_num(user_input, guess_num):
    if user_input in "aeiou":
        guess_num += 2
    else:
        guess_num += 1
    return guess_num


def get_unique_str(str):
    unique_secret_word = ""
    for i in str:
        if i not in unique_secret_word:
            unique_secret_word += i
    return unique_secret_word


def get_guess_score(secret_word, guess_num):
    unique_secret_word = get_unique_str(secret_word)
    return 10 - guess_num + len(unique_secret_word) * 4 + 3 * len(secret_word)


def print_dashes():
    print("-------------")


def get_choose_from(secret_word, letters_guessed):
    available_letters = get_available_letters(letters_guessed)
    unique_secret_word = get_unique_str(secret_word)
    choose_from = ""
    for i in unique_secret_word:
        if i in available_letters:
            choose_from += i
    return choose_from


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    guess_num = 0
    letters_guessed = []
    result = get_word_progress(secret_word, letters_guessed)
    while guess_num < 10:
        print_dashes()
        print(f"You have {10 - guess_num} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        user_input = input("Please guess a letter: ")  # todo: lower

        if input_is_legal(user_input, with_help):
            user_input = user_input.lower()
            if user_input == "!":
                if guess_num <= 7:
                    guess_num += 3
                    choose_from = get_choose_from(secret_word, letters_guessed)
                    new = random.randint(0, len(choose_from) - 1)
                    revealed_letter = choose_from[new]
                    print(f"Letter revealed: {revealed_letter}")
                    letters_guessed.append(revealed_letter)
                    result = get_word_progress(secret_word, letters_guessed)

                    if has_player_won(secret_word, letters_guessed):
                        print(f"Good guess: {result}")
                        print_dashes()
                        print("Congratulations, you won!")
                        print(
                            f"Your total score for this game is: {get_guess_score(secret_word, guess_num)}"
                        )
                        break
                    else:
                        print(result)
                else:
                    print(f"Oops! Not enough guesses left: {result}")
            else:
                if user_input not in letters_guessed:
                    letters_guessed.append(user_input)
                    if user_input in secret_word:
                        result = get_word_progress(secret_word, letters_guessed)
                        print(f"Good guess: {result}")
                        if has_player_won(secret_word, letters_guessed):
                            print_dashes()
                            print("Congratulations, you won!")
                            print(
                                f"Your total score for this game is: {get_guess_score(secret_word, guess_num)}"
                            )
                            break
                    else:
                        guess_num = increase_guess_num(user_input, guess_num)
                        print(f"Oops! That letter is not in my word: {result}")
                else:
                    print(f"Oops! You've already guessed that letter: {result}")
        else:
            print(
                f"Oops! That is not a valid letter. Please input a letter from the alphabet: {result}"
            )
    if not has_player_won(secret_word, letters_guessed):
        print_dashes()
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = "wildcard"  # choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
