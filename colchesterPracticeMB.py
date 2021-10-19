# Solve a null cipher based on every nth-letter in every nth-word.
# https://www.nostarch.com/impracticalpythonprojects (BSD Licensed)
# Takes an input, n, and checks for and displays a null cipher based
# on the nth letter after the start of every nth word.

# To see how this program would work, use the file colchester_message.txt
# which has is available here for your convenience.

import sys

def load_text(file):
    
    # Load a text file as a string.
    
    with open(file) as f:
        return f.read().strip()

# Load & process message:

filename = input("\nEnter full filename for message to translate: ")

try:
    loaded_message = load_text(filename)
except IOError as e:
    print("{}. Terminating program.".format(e), file=sys.stderr)
    sys.exit(1)

# Check loaded message & # of lines

print("\nORIGINAL MESSAGE = {}\n".format(loaded_message))

# Convert message to list and get length

message = loaded_message.split()
end = len(message)

# Get user input on interval to check

increment = int(input("Input max word & letter position to \
check (e.g., every 1 of 1, 2 of 2, etc.): "))
print()

# Find letters at designated intervals

for i in range(1, increment + 1):
    print("\nUsing increment letter {} of word {}".format(i, i))
    print()
    count = i - 1
    location = i - 1
    for index, word in enumerate(message):
        if index == count:
            if location < len(word):
                print("letter = {}".format(word[location]))
                count += i
            else:
                print("Interval doesn't work", file=sys.stderr)
