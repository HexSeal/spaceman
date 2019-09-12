#Spaceman project
import random
guesses = 8

def load_word():
    # A function that reads a text file of words and randomly selects one to use as the secret word
  
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    # A function that checks if all the letters of the secret word have been guessed.
  
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    # A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    got_letters = []
    for letter in secret_word:
        if letter in letters_guessed:
            got_letters += letter
        else: 
            got_letters += ("_")
    return got_letters


def is_guess_in_word(guess, secret_word):
    # A function to check if the guessed letter is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

def guess_again(new_guess, all_guesses):
    while new_guess in all_guesses:
        new_letter = input("\nAlready guessed! Please try again: ")
        new_guess = new_letter
        return new_guess

def spaceman(secret_word):
    # A function that controls the game of spaceman. Will start spaceman in the command line.

    print("\nWelcome to Spaceman(hangman)!")
    print("\nThe secret word has " + str(len(secret_word)) + " letters.") 
    print("You have " + str(len(secret_word)) + " guesses. Good Luck!")
    print("Guess one letter per round\n")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")    
    # print(secret_word)
    # Ask the player to guess one letter per round and check that it is only one letter
    running = True
    gotten_letters = []
    all_guesses = []
    guesses = 0

    while running == True:
        print("You have " + str((len(secret_word) - guesses)) + " guesses left!\n")

        guess = input("Please input a letter: ")
        while len(guess) != 1:
            print("Please enter only one letter")
            guess = input("Enter a letter: ")
            
        new_guess = guess
    # Checks if letter has already been guessed 
        if new_guess in all_guesses:
            guess_again(guess, all_guesses)

    # Check if the guessed letter is in the secret word or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("\nYou guessed correctly!\n")
            gotten_letters.append(guess)
            all_guesses.append(guess)
        else:
            print("\nWrong! Try again\n")
            all_guesses.append(guess)
            guesses += 1
    
    # Show the guessed word so far
        print("Your correct guesses this far are: ", get_guessed_word(secret_word, gotten_letters))
        print("All guesses: ", all_guesses)
        print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    # Check if the game has been won or lost
    
        if is_word_guessed(secret_word, gotten_letters):
            print("Congrats, you guessed the secret word!")
            function_code = input("Play Again? y/n: ")
            if function_code.lower() == "y":
                spaceman(load_word())

        if guesses == len(secret_word):
            print("Sorry, you lost.")
            print("Thank you for playing")
            print("The secret word was: ", secret_word)
            function_code = input("Play Again? y/n: ")
            if function_code.lower() == "y":
                spaceman(load_word())
                return True

secret_word = load_word()
spaceman(secret_word)

