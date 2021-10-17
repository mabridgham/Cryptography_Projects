# Cryptomath Module
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# Finds the Greates Common Divisor of two numbers a and b. Also finds the
# Modular Inverse of two numbers.
# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient 
# method for computing the greatest common divisor (GCD) of two integers (numbers),
# the largest number that divides them both without a remainder.
# To learn more about the Extended Euclidean Algorithm visit and why it is important 
# to cryptography https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

def gcd(a, b):
    
    # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
    
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    
    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # No mod inverse exists if a & m aren't relatively prime.

    # Calculate using the Extended Euclidean Algorithm:
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
