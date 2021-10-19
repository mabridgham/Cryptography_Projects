# One-Time Pad Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# The one-time pad cipher is a Vigenere Cipher that becomes unbreakable
# when the key meets the following criteria:
# 1. It is exactly as long as the encrypted message.
# 2. It is made up of truly random symbols.
# 3. It is used only once and never again for any other message.


import detectEnglishMB, secrets

print('''This program generates a one time pad that can be used as a key in the
Vigenere Cipher. For this to truly qualify as a one time pad however it must meet
the following qualifications:\n
1. It is exactly as long as the encrypted message.\n
2. It is made up of truly random symbols.\n
3. It is used only once and never again for any other message.\n
This program allows the user to input the message they intend to use in their
cipher and does not store it. It then uses that to generate a unique one time pad
each time this program is run, even if the same original message is used to
generate it. Once generated, simply copy and paste into your Vigenere Cipher to
use as your key once and only once to make your cipher unbreakable.''')


UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

message = input('Enter message to generate One-Time Pad: ')

lengthForKey = detectEnglishMB.removeNonLetters(message)

otp = ''
for i in range(len(lengthForKey)):
    otp += secrets.choice(UPPERLETTERS)

print(otp)
