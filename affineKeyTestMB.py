# Affine Key Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# The Affine Ciper is a type of monoalphabetic substitution cipher, where
# each letter in an alphabet is mapped to its numeric equivalent,
# encrypted using a simple mathematical function, and converted back to a letter.
# The formula used means that each letter encrypts to one other letter,
# and back again, meaning the cipher is essentially a standard substitution
# cipher with a rule governing which letter goes to which.


# This program proves that the keyspace of the affine cipher is limited
# to less than len(SYMBOLS) ^ 2.

import affineCipherMB, cryptomathMB

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 80):
    key = keyA * len(affineCipherMB.SYMBOLS) + 1

    if cryptomathMB.gcd(keyA, len(affineCipherMB.SYMBOLS)) == 1:
        print(keyA, affineCipherMB.encryptMessage(key, message))
