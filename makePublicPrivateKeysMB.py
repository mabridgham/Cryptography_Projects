# Public Key Generator
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# The Public Key algorithm creates two large random prime numbers and
# the uses complicated math (including finding a modular inverse) to create
# the public and private keys.

import random, sys, os, primeNumMB, cryptoMathMB


def main():

    # Create a public/private keypair with 1024-bit keys:

    print('Making key files...')
    makeKeyFiles('IT_bee', 1024)
    print('Key files made.')


def generateKey(keySize):

    # Creates public/private keys keySize bits in size.

    p = 0
    q = 0

    # Step 1: Create two prime numbers, p and q. Calculate n = p * q:

    print('Generating p prime...')
    while p == q:
        p = primeNumMB.generateLargePrime(keySize)
        q = primeNumMB.generateLargePrime(keySize)

    n = p * q

    # Step 2: Create a number e that is relatively prime to (p - 1) * (q - 1):

    print('Generating e that is relatively prime to (p - 1) * (q - 1)...')
    while True:
        # Keep trying random numbers for e until one is valid:
        e = random.randrange(2**(keySize-1), 2**(keySize))
        if cryptoMathMB.gcd(e, (p-1)*(q-1) == 1):
            break

    # Step 3: Calculate d, the mod inverse of e:

    print('Calculating d that is mod inverse of e...')
    d = cryptoMathMB.findModInverse(e, (p-1)*(q-1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)

    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):

    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
    # is the value in name) with the n, e and d, e integers written in
    # them, delimited by a comma.

    # Our safety check will prevent us from overwriting our old key files:

    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and rerun this program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    print()
    print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()


if __name__ == '__main__':
    main()
                            
