# Reverse Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# The Reverse Cipher encrypts a message by printing it in reverse order.
# So "Hello, world!" encrypts to "!dlrow ,olleH"

# Print greeting:

print("""The Reverse Cipher encrypts a message by printing it in reverse order.
So "Hello, world!" encrypts to "!dlrow ,olleH" To use this program, simply enter
your message below.\n""")

# Get message from user:

message = input('Enter message: ')

translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
