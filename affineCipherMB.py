# Affine Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# The Affine Ciper is a type of monoalphabetic substitution cipher, where
# each letter in an alphabet is mapped to its numeric equivalent,
# encrypted using a simple mathematical function, and converted back to a letter.
# The formula used means that each letter encrypts to one other letter,
# and back again, meaning the cipher is essentially a standard substitution
# cipher with a rule governing which letter goes to which.

import sys, pyperclip, cryptomathMB, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def main():
    
    myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    myKey = 2894
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (myMode))


def getKeyParts(key):
    
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
        
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
        
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
        
    if cryptomathMB.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            
            # Encrypt the symbol:
            
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # Append the symbol without encrypting.
            
    return ciphertext


def decryptMessage(key, message):
    
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomathMB.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            
            # Decrypt the symbol:
            
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # Append the symbol without decrypting.
            
    return plaintext


def getRandomKey():
    
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomathMB.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


# Call the main function:
if __name__ == '__main__':
    main()
