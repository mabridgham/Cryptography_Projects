# Simple Substitution Dictionary Hacker
# https://inventwithpython.com/hacking (BSD Licensed)
# The Substitution Cipher is a cipher in which the letters of the plaintext
# are systematically replaced by substitute letters.

import pyperclip, simpleSubKeywordMB , detectEnglishMB

SILENT_MODE = False

def main():
    
    myMessage = """SJITDOPIQR: JIR RIQMUNQRO AY P WDQC QCR NRSMRQN JT A SJITDORO QJ CRMNRGT AY S. -PHAMJNR ADRMSR"""

    brokenCiphertext = hackSimpleSubDictionary(myMessage)

    if brokenCiphertext == None:
        
        # hackSimpleSubDictionary() will return the None value if it was unable to hack the encryption.
        
        print('Hacking failed. Unable to hack this ciphertext.')
        
    else:
        
        # The plaintext is displayed on the screen. For the convenience of the user, we copy the text of the code to the clipboard.
        
        print('Copying broken ciphertext to clipboard:')
        print(brokenCiphertext)
        pyperclip.copy(brokenCiphertext)


def hackSimpleSubDictionary(message):
    
    print('Hacking with %s possible dictionary words...' % (len(detectEnglishMB.ENGLISH_WORDS) * 3))

    # Python programs can be stopped at any time by pressing Ctrl-C (on Windows) or Ctrl-D (on Mac and Linux)

    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    tryNum = 1

    # Brute-force by looping through every possible key

    for key in detectEnglishMB.ENGLISH_WORDS:
        if tryNum % 100 == 0 and not SILENT_MODE:
            print('%s keys tried. (%s)' % (tryNum, key))

        decryptedText = simpleSubKeywordMB.decryptMessage(key, message)

        if detectEnglishMB.getEnglishCount(decryptedText) > 0.20:

            # Check with the user to see if the decrypted key has been found.

            print()
            print('Possible encryption hack:')
            print('Key: ' + str(key))
            print('Decrypted message: ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

        tryNum += 1

    return None

if __name__ == '__main__':
    main()
