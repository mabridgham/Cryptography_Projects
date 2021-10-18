# Simple Substitution Keyword Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# The Substitution Cipher is a cipher in which the letters of the plaintext
# are systematically replaced by substitute letters. Use a keyword as a key.

import pyperclip, simpleSubCipherMB

def main():
    
    myMessage = """Your cover is blown."""
    myKey = 'alphanumeric'
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'


    print('The key used is:')
    print(makeSimpleSubKey(myKey))

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('The %sed message is:' % (myMode))
    print(translated)

    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')


def encryptMessage(key, message):
    
    key = makeSimpleSubKey(key)
    return simpleSubCipherMB.encryptMessage(key, message)


def decryptMessage(key, message):
    
    key = makeSimpleSubKey(key)
    return simpleSubCipherMB.decryptMessage(key, message)


def makeSimpleSubKey(keyword):
    
    # Create the key from the keyword
    
    newKey = ''
    keyword = keyword.upper()
    keyAlphabet = list(simpleSubCipherMB.LETTERS)
    for i in range(len(keyword)):
        if keyword[i] not in newKey:
            newKey += keyword[i]
            keyAlphabet.remove(keyword[i])
    key = newKey + ''.join(keyAlphabet)
    return key


if __name__ == '__main__':
    main()
