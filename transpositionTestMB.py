# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# A Transposition Cipher is a cipher in which the letters of the plaintext
# are systematically rearranged into another sequence.

# Test to see if the transposition cipher works and is valid.

import random, sys, transpositionEncryptMB, transpositionDecryptMB

def main():

    random.seed(42) # Set the random "seed" to a static value.

    for i in range(20): # Run 20 tests.

        # Generate random messages to test.

        # The message will have a random length:

        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it:

        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # Convert the list back to a string.

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message:

        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncryptMB.encryptMessage(key, message)
            decrypted = transpositionDecryptMB.decryptMessage(key, encrypted)

            # If the decryption doesn't match the original message, display
            # an error message and quit:

            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')


# Call the main function:

if __name__ == '__main__':
    main()
