# Caesar Cipher
# https://nostarch.com/crackingcodes/ (BSD Licensed)
# Named after Julius Caesar, the Caesar cipher is one of the oldest ciphers and is based on the
# simplest monoalphabetic cipher. A Caesar cipher is categorized as a substitution cipher
# in which the alphabet in the plain text is shifted by a fixed number down the alphabet.

import pyperclip

# Print greeting:

print('Named after Julius Caesar, the Caesar Cipher is one of the oldest ciphers and is based on the')
print('simplest monoalphabetic cipher. A Caesar cipher is categorized as a substitution cipher')
print('in which the alphabet in the plain text is shifted by a fixed number down the alphabet.\n')
print('While the original Caesar Cipher only uses only letters, this program adds symbols to the')
print('list as well as letters allowing for not only more complex messages but a longer and stronger keyspace.\n')
print('To use this program, Enter the message you wish to either encrypt or decrypt. Then choose the value')
print('of the shift by choosing a number between 1 and 95.\n')


# The string to be encrypted/decrypted:

message = input('Enter message: ')

# The encryption/decryption key:

key = int(input('Enter a number between 1 - 94: ')) # Key can be any number integer from 0 to 94 and represents the amount of shift.

# Whether the program encrypts or decrypts:

mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted:

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz[\\]^_`{|}~ !"#$%&\'()*+,-./0123456789:;<=>?@'

# Store the encrypted/decrypted form of the message:

translated = ''

for symbol in message:
    
    # Note Only symbols in the SYMBOLS string can be encrypted/decrypted.

    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed:

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:

        # Append the symbol without encrypting/decrypting:

        translated = translated + symbol

# Output the translated string:

print(translated)
pyperclip.copy(translated)
