import string

def load_words(file_name):

    # print("Loading word list from file...")
    # inFile: file
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


def get_story_string():

    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def _init_(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def get_message_text(self):

        return self.message_text


    def get_valid_words(self):
  
        valid_words_copy = self.valid_words.copy()
        return valid_words_copy


    def build_shift_dict(self,shift):

        mapping_dict = {}
        lower_case = list(string.ascii_lowercase)
        upper_case = list(string.ascii_uppercase)
        overflow = 0
        for i in range(26):
            for letter in lower_case:
                new_pos = lower_case.index(letter)+shift               
                if new_pos < 26:
                    mapping_dict[letter] = lower_case[new_pos]
                else:
                    overflow = new_pos-26
                    mapping_dict[letter] = lower_case[overflow]
        overflow = 0
        for i in range(26):
            for letter in upper_case:
                new_pos = upper_case.index(letter)+shift
                if new_pos < 26:
                    mapping_dict[letter] = upper_case[new_pos]
                else:
                    overflow = new_pos-26
                    mapping_dict[letter] = upper_case[overflow]
        
        return mapping_dict



    def apply_shift(self, shift):

        mapping_dict = self.build_shift_dict(shift)

        text_list = list(self.get_message_text())
        new_word = []

        try:
            for letter in text_list:
                new_word.append(mapping_dict[letter])
        except:
            pass
        return "".join(new_word)



class PlaintextMessage(Message):
    def __init__(self, text, shift):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        
        return self.shift

    def get_encryption_dict(self):
        
        encryption_dict_copy = self.encryption_dict.copy()
        return encryption_dict_copy

    def get_message_text_encrypted(self):

        return self.message_text_encrypted
        

    def change_shift(self, shift):
        self.shift = shift
        


class CiphertextMessage(Message):
    def __init__(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):

        for i in range(26):
            current_word = self.apply_shift(26-i)
            if is_word(self.valid_words,current_word):
                return (26-i,current_word)
    
    def decrypt_message_withvalue(self,shifts): #self made method to make the story deciphering work

        current_word = self.apply_shift(shifts)
        if is_word(self.valid_words,current_word):
            return (shifts,current_word)
    

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print('------------------------------')
    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    #TODO: WRITE YOUR TEST CASES HERE
    print('------------------------------')
    plaintext = PlaintextMessage('apple',10)
    print('Expected Output: kzzvo')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print('------------------------------')
    ciphertext = CiphertextMessage('kzzvo')
    print('Expected Output:', (16, 'apple'))
    print('Actual Output:', ciphertext.decrypt_message())    

#TODO: best shift value and unencrypted story 
    story = get_story_string().split(" ")
    shiftValues = []
    for word in story:
        ciphertext = CiphertextMessage(word)
        if ciphertext.decrypt_message() != None:
            shift_value = ciphertext.decrypt_message()[0]
            words = ciphertext.decrypt_message()[1]
            shiftValues.append(shift_value)
        else:
            continue

    max_occurance = max(set(shiftValues), key = shiftValues.count)
    print('---------------------------')
    print("shift value: ",max_occurance)
    for word in story:
        current_word = CiphertextMessage(word)
        # current_word.change_shift(max_occurance)
        if current_word.decrypt_message_withvalue(max_occurance) != None:
            words = current_word.decrypt_message_withvalue(max_occurance)[1]
            print(words,end=" ")
        else:
            continue
