# Simple Substitution Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# The Substitution Cipher is a cipher in which the letters of the plaintext
# are systematically replaced by substitute letters.

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():

    myMessage = input('Enter message: ') # Allow the user to enter message.
    myKey = getRandomKey() # Get random key
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'.

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')


def keyIsValid(key):

    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key, message):

    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):

    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):

    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':

        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.

        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message:

    for symbol in message:
        if symbol.upper() in charsA:

            # Encrypt/decrypt the symbol:

            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:

            # Symbol is not in LETTERS; just add it:
            
            translated += symbol

    return translated


def getRandomKey():

    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
