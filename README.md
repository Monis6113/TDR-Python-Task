# TDR-Python-Task
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    inFile = open(WORDLIST_FILENAME,"r")
    line = inFile.readline()
    wordlist = line.split()
    print(" ",len(wordlist),"Words loaded.\n-------------------\n")
    return wordlist


def choose_word(wordlist):

    return random.choice(wordlist) 


def is_word_guessed(secret_word, letters_guessed):
    secret_word_list = []
    for letter in secret_word:
        secret_word_list.append(letter)
    if (set(secret_word_list).issubset(set(letters_guessed))):
        return True
    else:
        return False


def is_letter_in_word(letter_inputed,secret_word):
    
    if letter_inputed in secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word,letters_guessed):
    position_list = []    
    my_word = [] 

    for letter in letters_guessed:
        if letter in secret_word:
            position = secret_word.index(letter)
            position_list.append(position)

    for letter in secret_word:
        if secret_word.index(letter) in position_list:
            my_word.append(letter)
        else:
            my_word.append(" _")
    print(f"\n"," ".join(my_word),"\n")
    return(my_word)


def get_available_letters(letters_guessed):
    letters = string.ascii_lowercase
    letter_list = list(letters)
    for letter in letters_guessed:
        letter_list.remove(letter)
    print('\n',"".join(letter_list),'\n---------------------------')    


def show_possible_matches(my_word,secret_word):

    inFile = open(WORDLIST_FILENAME,"r")
    line = inFile.readline()
    wordlist = line.split()
    # letter_index_dict = {}
    possible_matches = []
    # values = []
    for letter in my_word:
        if letter != " _":
            position = my_word.index(letter)
            for word in wordlist:
                if len(word) == len(secret_word):
                    if word[position] == letter:
                        possible_matches.append(word)
    # for letter in my_word:
    #     if letter != " _":
    #         letter_index_dict[letter] = values.append(my_word.index(letter))
    # match = False
    # print(letter_index_dict)
    # for word in wordlist:
    #     if len(word) == len(secret_word):
    #         for letter in word:
    #             try:
    #                 if word.index(letter) == letter_index_dict.get(letter,None):
    #                     match = True
    #                 else:
    #                     match = False 
    #             except:
    #                 pass
    #         if match == True:
    #             possible_matches.append(word)
            
    return possible_matches


def hangman(secret_word):
    guesses_left = 6
    warnings = 3
    letters_guessed = []
    print(f"I am thinking of a {len(secret_word)} letter word!")
    
    letters_guessed = []
    vowels = ['a','e','i','o','u']

    while is_word_guessed(secret_word,letters_guessed) == False:
        
        print(f"You have {guesses_left} guesses left.")
        print(f"You have {warnings} warnings left.")

        letter_inputed = input("Please guess a letter: ")
        letter_inputed = str.lower(letter_inputed)      

        if len(letter_inputed) == 1:
            if str.isalpha(letter_inputed) is True:

                if letter_inputed not in letters_guessed: 
                    letters_guessed.append(letter_inputed)
                    last_input = True

                else:
                    if warnings > 0:
                        warnings -= 1
                    else:
                        warnings = 0
                        guesses_left = guesses_left-1
                    
                    print(f"oops! you have already guessed that letter. You now have {warnings} warnings left.")
                    get_guessed_word(secret_word,letters_guessed)
                    
                    last_input = False

            else:
                if letter_inputed != "*":
                    if warnings > 0:
                        warnings -= 1
                    else:
                        warnings = 0
                        guesses_left -= 1
                    print(f"oops! That is not a valid letter. You have {warnings} warnings left.")
                    get_guessed_word(secret_word,letters_guessed)
                else:
                    if len(letters_guessed) != 0:
                        my_word = get_guessed_word(secret_word,letters_guessed)
                        print(show_possible_matches(my_word,secret_word))
                    else:
                        print("\nCant show matches for 0 guesses done.\n")
                        guesses_left -= 1
                last_input = False
        
            if last_input == True:
                if is_letter_in_word(letter_inputed,secret_word) is False:
                    if letter_inputed in vowels:
                        guesses_left -= 2
                    else:
                        guesses_left -= 1

                    print("oops! That letter is not in my word!")
                    get_available_letters(letters_guessed)
                    get_guessed_word(secret_word,letters_guessed)
                else:
                    get_available_letters(letters_guessed)
                    print("Good guess",end=": ")
                    get_guessed_word(secret_word,letters_guessed)

        else:
            print("\nPlease enter a single valid alphabet. ")
            guesses_left -= 1
        
        
        if is_word_guessed(secret_word,letters_guessed) == True:
            total_score = guesses_left*len(set(secret_word))
            print(f"You won!\nYour total score was {total_score}.")
            break

        if guesses_left == 0:
            print(f"Sorry, you ran out of guesses!\nSecret word was {secret_word}.")   
            break

 
         
if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    # secret_word = "apples"
    hangman(secret_word)




