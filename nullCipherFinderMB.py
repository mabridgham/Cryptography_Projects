# Decode a null cipher based on number of letters after punctuation marks.
# https://www.nostarch.com/impracticalpythonprojects (BSD Licensed)

# This program is based on the Trevanion Cipher. The Trevanion Cipher originally used
# the third letter after punctuation to create a message. You can use a different text
# and offset other than 3 to look for hidden messages in other documents. For the
# purpose of demonstration, the original letter sent to Sir John Trevanion to help
# him escape moments before his execution in 1642 has been included here called
# trevanion.txt.

import string
import sys


def load_text(file):
    # Load a text file as a string.

    with open(file) as f:
        return f.read().strip()


def solve_null_cipher(message, lookahead):
    # Solve a null cipher based on number letters after punctuation mark.
    # message = null cipher text as string stripped of whitespace
    # lookahead = endpoint of range of letters after punctuation mark to examine

    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Using offset of {} after punctuation = {}".format(i, plaintext))
        print()


def main():
    # Load text, solve null cipher.

    # Load & process message:

    filename = input("\nEnter full filename for message to translate: ")
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print("{}. Terminating program.".format(e), file=sys.stderr)
        sys.exit(1)
    print("\nORIGINAL MESSAGE =")
    print("{}".format(loaded_message), "\n")
    print("\nList of punctuation marks to check = {}".
          format(string.punctuation), "\n")

    # Remove whitespace:

    message = ''.join(loaded_message.split())

    # Get range of possible cipher keys from user:

    while True:
        lookahead = input("\nNumber of letters to check after "
                          "punctuation mark: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input a number.", file=sys.stderr)
    print()

    # Run function to decode cipher:

    solve_null_cipher(message, lookahead)


if __name__ == '__main__':
    main()
