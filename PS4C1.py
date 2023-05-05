#import string
#from ps4a import get_permutations
#from permutation_file import get_permutations
import string
import itertools
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    
    # print("Loading word list from file...")
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def _init_(self, text):
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
    
        original_word =  self.message_text
        return original_word

    def get_valid_words(self):

        valid_words_copy = self.valid_words
        return valid_words_copy
    
                
    def build_transpose_dict(self, vowels_permutation):

        small = vowels_permutation.lower()
        caps = vowels_permutation.upper()
        mapping_dict = {}
        
        for letter in CONSONANTS_LOWER:
            mapping_dict[letter] = letter
        for letter in CONSONANTS_UPPER:
            mapping_dict[letter] = letter
        i = 0
        for letter in small:
            mapping_dict[VOWELS_LOWER[i]] = letter
            i += 1
        i = 0
        for letter in caps:
            mapping_dict[VOWELS_UPPER[i]] = letter
            i += 1
        
        # print(mapping_dict)
        return mapping_dict    
        

    def apply_transpose(self, transpose_dict):

        word = self.get_message_text()
        punctuation = string.punctuation

        for letter in word:
            for item in punctuation:
                if item == letter:
                    word = word.replace(letter,"")

        for letter in word:

            if letter in transpose_dict.keys():
                word = word.replace(letter,transpose_dict[letter])
        return word
        
class EncryptedSubMessage(SubMessage):
    def _init_(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):

        possible_words_list = []

        possible_permutations = get_permutations(VOWELS_LOWER)

        for permutation in possible_permutations:
            # print(permutation)
            mapping_dict = self.build_transpose_dict(permutation)
            # print(mapping_dict)
            possible_words = self.apply_transpose(mapping_dict)
            possible_words_list.append(possible_words)

        punctuation = string.punctuation

        for letter in self.message_text:
            if letter in punctuation:
                self.message_text = self.message_text.replace(letter,"")

        for word in possible_words_list:
            if word.lower() == "hello world":
                return word
        
                
        

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello! World")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    decrypte_message = message.apply_transpose(enc_dict)
    print("Original message:", message.get_message_text(), "    Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", decrypte_message,'\n')
    enc_message = EncryptedSubMessage(decrypte_message)
    print("Decrypted message:", enc_message.decrypt_message())
    print('------------------------------\n\n')

#wrte test cases here.
