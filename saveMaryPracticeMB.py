# http://www.nostarch.com/impracticalpythonprojects (BSD Licensed)
# Help to change the fate of Mary, Queen of Scots. She has been imprisoned
# and the only way to send her messages is through the traitorous Gilbert Gifford.
# Use a null cipher to hide a message within a list of names using a variable pattern.

# This program uses a list of names in a file 'supporters.txt' to hide the cipher
# message. It has been included here to run the program.

import load_dictionaryMB

# Write a short message and use no punctuation or numbers!

message = "Give your word and we rise"
message = "".join(message.split())

# Open name file

names = load_dictionaryMB.load('supporters.txt')

name_list = []

# Start list with null word not used in cipher

name_list.append(names[0])

# Add letter of null cipher to 2nd letter of name, then 3rd, then repeat

count = 1
for letter in message:
    for name in names:
        if len(name) > 2 and name not in name_list:
            if count % 2 == 0 and name[2].lower() == letter.lower():
                name_list.append(name)
                count += 1
                break
            elif count % 2 != 0 and name[1].lower() == letter.lower():
                name_list.append(name)
                count += 1
                break

# Add two null words early in message to throw-off cryptanalysts

name_list.insert(3, 'Stuart')
name_list.insert(6, 'Jacob')

# Display cover letter and list with null cipher

print("""
Your Royal Highness: \n
It is with the greatest pleasure I present the list of noble families who
have undertaken to support your cause and petition the usurper for the
release of your Majesty from the current tragical circumstances.
""")

print(*name_list, sep='\n')        
  
