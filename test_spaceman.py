from spaceman import is_word_guessed, is_guess_in_word, get_guessed_word

def test_get_guessed_word():
    secret_word = ['m', 'a', 'x']
    letters_guessed = ['m', 'x']

    assert get_guessed_word(
    secret_word, letters_guessed) == True, 'get_guessed_word is not working as intended'

def test_is_word_guessed():
    # Set up
    secret_word = 'cat'
    letters_guessed = ['c','a','t']

    #test
    assert is_word_guessed(
        secret_word, letters_guessed) == True, 'is_word_guessed function is not working as intended'


def test_is_guess_in_word():
    # A function to check if the guessed letter is in the secret word
    guess = 'd'
    secret_word = 'desk'

    assert is_guess_in_word(
        guess, secret_word) == True, 'guess_in_word is not working as intended'
    
