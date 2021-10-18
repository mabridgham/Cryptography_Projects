# Affine Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# The Affine Ciper is a type of monoalphabetic substitution cipher, where
# each letter in an alphabet is mapped to its numeric equivalent,
# encrypted using a simple mathematical function, and converted back to a letter.
# The formula used means that each letter encrypts to one other letter,
# and back again, meaning the cipher is essentially a standard substitution
# cipher with a rule governing which letter goes to which.

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False


def main():

    myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
        
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
        
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key
    
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            
            # Check with the user if the decrypted key has been found.
            
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
            
    return None


# Call main function:
if __name__ == '__main__':
    main()
