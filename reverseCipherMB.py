# Reverse Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# The Reverse Cipher encrypts a message by printing it in reverse order.
# So "Hello, world!" encrypts to "!dlrow ,olleH"

# Get message from user:

message = input('Enter message: ')

translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
