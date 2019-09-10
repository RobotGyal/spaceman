import random

import pyfiglet

letters_guessed = []

class colors:
    purple = '\033[30m'
    green = '\033[32m'
    yellow = '\033[93m'
    pink = '\033[95m'
    grey = '\033[37m'
    red = '\033[31m'


#RANDOMLY PICKS A WORD FROM WORDS.TXT FILE
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


#CHECKS IF ALL LETTERS GUESSED IN WORD
def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    show = [x for x in secret_word if x in letters_guessed]

    if len(show) == len(secret_word):
        return True
    else:
        return False

#DISPLAYS WORD WITH CORRECT GUESSES OR BLANKS
def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    guesses = []

    for letter in secret_word:
        show = set(letters_guessed).intersection(secret_word)
        if letter in show:
            guesses.append(letter)
        else:
            guesses.append('_ ')

    answer = ''.join(guesses)
    print('This is the correct answer: ' + answer)

#CHECK IF GUESS LETTER IS IN WORD
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    if guess in secret_word and guess not in letters_guessed:
        letters_guessed.append(guess)
        print(colors.green, '\nYou have made a correct guess\n')
        return True
    elif guess in letters_guessed:
        print (colors.red, 'Letter already guessed. Try another letter\n')
        return False
    else:
        letters_guessed.append(guess)
        print (colors.red, '\nThat is not a correct letter')
        letters_guessed.sort()
        print('Here are the already guessed letters: ', *letters_guessed)
        return False


#REPLAYS GAME
#def replay():
    play_again = input('Would you like to play again? Choose an option: Y / N\n')
    if play_again == 'y' or play_again == 'Y':
        return True
    else:
        return False


#MAIN SPACEMAN FUNCTION
def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    
    welcome = '\n\nWelcome to Spaceman! \nA word guessing game of the new age!\nLet\'s get started!\n\n'
    banner_intro = pyfiglet.figlet_format(welcome, font = "drpepper" ) 
    banner_win = pyfiglet.figlet_format('You Win!!', font = "drpepper" ) 
    banner_lose = pyfiglet.figlet_format('You Lose!', font = "drpepper" ) 
    print(colors.yellow, banner_intro)

    while True: 
        print(colors.grey)
        print('Your word will be ' + str(len(secret_word)) + ' letters long')
        guess = input('Enter a letter: ').lower()
        if guess.isalpha() == False: #checks numbers and empty string
            print(colors.red, 'Please enter a letter only ')
        elif len(guess) > 1: #checks for only 1 character
            print (colors.red, 'Enter only 1 letter at a time ')
        else:
            is_guess_in_word(guess, secret_word)
            get_guessed_word(secret_word, letters_guessed)
            incorrect_guess = set(letters_guessed).difference(secret_word)

            if is_word_guessed(secret_word, letters_guessed) == True:
                print(colors.pink, banner_win + '\nYou won the game! Congratulations!')
                return False
                #replay()
            elif len(incorrect_guess) > 6:
                print(colors.red, banner_lose + '\nYou lost.\nThis is your mystery word: ' + secret_word + '\nBetter luck next time.')
                return False
                #replay()
            else:
                print (colors.yellow, "Number of guesses attempted: " + str(len(incorrect_guess)) + '\n\n')


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
        


#FIX
#"this is the correct answer" to show the full word at the end
#"wrong guess" message even when correct guess is made
