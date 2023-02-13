from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from Crypto.PublicKey import ECC, RSA, ElGamal
from ElGamalsupport import ElGamal_keygen, ElGamal_param_load


def RSAkeygen():
    #TODO: generate a pair of key of 2048 bits

    #TODO: export keys to file


def RSAkeyload():
    #TODO: load generated RSA keys from file
    # you should change the following two lines.
    skey = 0
    pkey = 0
    return skey, pkey

def RSAencrypt(msg, key):
    #TODO: use the encryption API to encrypt
    # you should change the following line
    ciphertext = msg
    return ciphertext

def RSAdecrypt(ciphertext, key):
    #TODO: use the decryption API to decrypt
    # you should change the following line
    plaintext = ciphertext
    return plaintext


def ElGamalencrypt(msg, pk, g, p):
    # TODO: pick a temporary private key
    
    # TODO: calculate the temporary shared key
    
    # TODO: calculate the ciphertext components, c1 and c2
    
    # TODO: compose ciphertext
    # you should change the following line
    ciphertext = msg
    return ciphertext

def ElGamaldecrypt(ciphertext, sk, g, p):
    # TODO: parse the ciphertext into c1 and c2

    # TODO: recover temporary key shared between two entities for this encryption

    # TODO: calculate the plaintext from c2
    # you should change the following line
    plaintext = ciphertext
    return plaintext

def group_of_prime_order(bits = 256):
    # this is a function to find a group of prime order p, and its generator, g
    # you should use the code from ElGamal.py https://github.com/Legrandin/pycryptodome/blob/8bba4a056fb6b5cb7cc9616da3d36893f759efe8/lib/Crypto/PublicKey/ElGamal.py
    from Crypto.Math.Primality import ( generate_probable_safe_prime,
                                    test_probable_prime, COMPOSITE )
    from Crypto.Math.Numbers import Integer
    # TODO: randomly pick a large prime, p
    p = 61
    # TODO: find generator g of the group of prime order p
    g = 2


    # Found
    return p, g

def DHKE():
    #set up system parameter: pick group order, i.e., a prime, pick group generator, g
    # hint: for testing the code, you can pick a small g and p to start with
    # hint: for a secure parameter, you can reuse the code from ElGamal.py to pick the p and g
    # ElGamal.py https://github.com/Legrandin/pycryptodome/blob/8bba4a056fb6b5cb7cc9616da3d36893f759efe8/lib/Crypto/PublicKey/ElGamal.py

    p, g = group_of_prime_order()

   
    # TODO: generate a pair of public and private key for A

    # TODO: generate a pair of public and private key for B


    # using the public keys and the private keys to establish a shared key.

    # check that A and B have the same key now




def RSAsystem():
    RSAkeygen()
    # a message to send
    data = data = b"I met aliens in UFO. Here is the map. I send you this with RSA enryption"
    sk, pk = RSAkeyload()

    # TODO: call the encryption function you write above

    
    # TODO: call the decryption function you write above
    RSAdec = ''
    # compare the decrypted text is the same as sent data
    print(RSAdec, data == RSAdec)

def ElGamalsystem():
    # TODO: generate ElGamal keys. Use ElGamalsupport.py
    # a number to send
    data = 18
    # TODO: load generated ElGamal system parameters and keys

    # call the encryption function you write above
    ElGamalenc = ElGamalencrypt(data, pk, g, p)
    print(ElGamalenc)
    # call the decryption function you write above
    ElGamaldec = ElGamaldecrypt(ElGamalenc, sk, g, p)
    # compare the decrypted text is the same as sent data
    print(ElGamaldec, ElGamaldec == data)


def key_exchange_with_key_encap():
    # assume A has generated a symmetric key and wants to share it with B; B is the recipient of a symmetric key, e.g. a new session key
    # TODO: A generates the session key

    # assume B has an RSA key pair (sk, pk), which you can load from the key file you generated for RSA encryption exercise
    # A is able to access B's public key, as it is publicly accessible
    # TODO: load key from file

    # TODO: A encrypts session key for B - goal: confidentiality of the B

    # TODO: B decrypts

    # check key is shared


RSAsystem()
ElGamalsystem()
DHKE()
key_exchange_with_key_encap()



def timing(): 
    # this is a function to help you obtain the time it takes on average to run some code. You can use this for TASK 1.1-2-c
    no_of_instance = 1000

    from time import time
    start = time()
    for i in range(1,no_of_instance+1):
        #TODO
        if i%(int(no_of_instance/100)) == 0:
            print(i/int(no_of_instance/100), 'per cent done')
            end = time()
            runtime = end - start
            print('average time for one instance:',runtime/i)
    end = time()
    runtime = end - start
    print('average time for one instance:',runtime/no_of_instance)