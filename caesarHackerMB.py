# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# Named after Julius Caesar, the Caesar cipher is one of the oldest cipers and is based on the
# simplest monoalphabetic cipher. A Caesar cipher is categorized as a substitution cipher
# in which the alphabet in the plain text is shifted by a fixed number down the alphabet.

# Print greeting:

print("""Named after Julius Caesar, the Caesar Cipher is one of the oldest ciphers and is based on the
simplest monoalphabetic cipher. A Caesar cipher is categorized as a substitution cipher
in which the alphabet in the plain text is shifted by a fixed number down the alphabet.\n
To use this program, enter a message encrypted with the Caesar Cipher program. This program
tests and displays the results for every possible shift value. Scroll down the list until
you see a translated message.\n""")

# Get message from user:

message = input('Enter message to be decoded: ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz[\\]^_`{|}~ !"#$%&\'()*+,-./0123456789:;<=>?@'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is almost the same as the original program:

    # Loop through each symbol in `message`:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
