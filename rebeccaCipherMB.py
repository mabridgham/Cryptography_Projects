# Rebecca Book Cipher
# https://www.nostarch.com/real-world-python (BSD Licensed)
# The Rebecca Book Cipher is a variation of the one time pad cipher used
# by Nazi spies during World War II.
# The original Cipher used the book Rebecca by Daphne du Maurier as the key.
# Since that book is not available in the public domain this program will
# use a book file chosen by the user.

# There are many free open source books available online for download. It is interesting
# to try different ones and see how the cipher works or doesn't depending on the message
# you choose. This is because it uses the words in the book to create the cipher. If the
# word you choose is not in the book it can not use it. I have added a few books to try
# for this reason. The Hound of the Baskervilles by Sir Arthur Conan Doyle (hound.txt),
# The Lost World by Sir Arthur Conan Doyle (lost.txt), and War of the Worlds by
# H. G. Wells.

import sys, os, random, string
from collections import defaultdict, Counter

# Print greeting:

print('''To use, enter either a short plaintext message or the encrypted text you wish
to decrypt. Then choose which operation you would like to perform (encrypt or decrypt).
Choose the amount of shift you wish to use. In the original book version of this cipher
this represented the day of the year and therefore the page number in the book that the
person would use. This doesn't translate to a digital version but is still an effective
way to use the cipher as a one time pad. Finally, input the filename of the book you wish
to use with a .txt extension.\n
When encrypting, your message will be translated into a series of numbers. This is your cipher.
When decrypting, copy this code into the message input and choose decrypt along with the same
number shift you previously used to create the code and the same file name to see the
translated message.\n''')


def main():

    message = input("Enter plaintext or ciphertext: ")
    process = input("Enter 'encrypt' or 'decrypt': ")
    shift = int(input("Shift value(1-365) = "))
    infile = input("Enter filename with extension: ")

    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)
    word_list = load_file(infile)
    word_dict = make_dict(word_list, shift)
    letter_dict = make_letter_dict(word_list)

    if process == 'encrypt':
        ciphertext = encrypt(message, word_dict, letter_dict)
        count = Counter(ciphertext)
        encryptedWordList = []
        for number in ciphertext:
            encryptedWordList.append(word_list[number - shift])

        print("\nencrypted word list = \n {} \n".format(''.join(encryptedWordList)))
        print("encrypted ciphertext = \n {} \n".format(ciphertext))

        # Check the encryption by decrypting the ciphertext:

        print("decrypted plaintext = ")
        singleFirstCheck = False
        for cnt, i in enumerate(ciphertext):
            if word_list[ciphertext[cnt]-shift] == 'a' and \
               word_list[ciphertext[cnt+1]-shift] == 'a':
                continue
            if word_list[ciphertext[cnt]-shift] == 'a' and \
               word_list[ciphertext[cnt-1]-shift] == 'a':
                singleFirstCheck = True
                continue
            if singleFirstCheck == True and cnt<len(ciphertext)-1 and \
               word_list[ciphertext[cnt]-shift] == 'the' and \
               word_list[ciphertext[cnt+1]-shift] == 'the':
                continue
            if singleFirstCheck == True and \
               word_list[ciphertext[cnt]-shift] == 'the' and \
               word_list[ciphertext[cnt-1]-shift] == 'the':
                singleFirstCheck = False
                print('', end='', flush=True)
                continue
            if singleFirstCheck == True:
                print(word_list[i - shift][0], end='', flush=True)
            if singleFirstCheck == False:
                print(word_list[i-shift], end='', flush=True)
    elif process == 'decrypt':
            plaintext = decrypt(message, word_list, shift)
            print("\ndecrypted plaintext = \n {}".format(plaintext))


def load_file(infile):

    # Read and return text file as a list of lowercase words.

    with open(infile, encoding='utf-8') as file:
        words = [word.lower() for line in file for word in line.split()]
        words_no_punct = ["".join(char for char in word if char not in \
                                  string.punctuation) for word in words]
        
    return words_no_punct


def make_dict(word_list, shift):
    
    # Return dictionary of characters as keys and shifted indexes as values.
    
    word_dict = defaultdict(list)
    for index, word in enumerate(word_list):
        word_dict[word].append(index + shift)

    return word_dict
        

def make_letter_dictQC(firstLetterDict):

    sm = 0
    for letter in firstLetterDict.keys():
        sm += len(firstLetterDict[letter])
##        print(repr(letter), len(firstLetterDict[letter]))
##    print('Words starting with numbers are not counted...\n')

    return


def make_letter_dict(word_list):
    
    firstLetterDict = defaultdict(list)
    for word in word_list:
        if len(word) > 0:
            if word[0].isalpha():
                firstLetterDict[word[0]].append(word)
    make_letter_dictQC(firstLetterDict)
    
    return firstLetterDict


def encrypt(message, word_dict, letter_dict):
    
    # Return list of indexes representing characters in a message.

    encrypted = []
    
    # Remove punctuation from message words
    
    messageWords = message.lower().split()
    messageWordsNoPunct = ["".join(char for char in word if char not in \
                                 string.punctuation) for word in messageWords]
    
    for word in messageWordsNoPunct:
        if len(word_dict[word]) > 1:
            index = random.choice(word_dict[word])
        elif len(word_dict[word]) == 1:  # Random.choice fails if only 1 choice.
            index = word_dict[word][0]
        elif len(word_dict[word]) == 0:  # Word not in word_dict.
            encrypted.append(random.choice(word_dict['a']))
            encrypted.append(random.choice(word_dict['a']))
            for letter in word:
                if letter not in letter_dict.keys():
                    print('\nLetter {} not in letter-to-word dictionary.'
                          .format(letter), file=sys.stderr)
                    continue
                if len(letter_dict[letter])>1:
                    newWord =random.choice(letter_dict[letter])
                else:
                    newWord = letter_dict[letter][0]
                if len(word_dict[newWord])>1:
                    index = random.choice(word_dict[newWord])
                else:
                    index = word_dict[newWord][0]
                encrypted.append(index)
                
            encrypted.append(random.choice(word_dict['the']))
            encrypted.append(random.choice(word_dict['the']))
            continue
        encrypted.append(index)
        
    return encrypted


def decrypt(message, word_list, shift):
    
    # Decrypt ciphertext string and return plaintext word string.
    # This shows how plaintext looks before extracting first letters.
    
    plaintextList = []
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()]
    
    for count, i in enumerate(indexes):
        plaintextList.append(word_list[int(i) - shift])
        
    return ' '.join(plaintextList)


def check_for_fail(ciphertext):
    
    # Return True if ciphertext contains any duplicate keys.
    
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        print(check)
        return True


if __name__ == '__main__':
    main()

