def caesar_enc(msg,key):
    # caesar cipher encryption function
    cipher = ''
    for c in msg:
        if (c == ' '):
            cipher += ' '
        else:
            c = ord(c)
            if (c <= ord('Z')) and (c>= ord('A')):
                c = (c - ord('A')  + key) % 26
                cipher += chr(c + ord('A'))
            if (c <= ord('z')) and (c>= ord('a')):
                c = (c - ord('a')  + key) % 26
                cipher += chr(c + ord('a'))
    return cipher

def caesar_dec(cipher,key):
    # caesar cipher decryption function
    msg = ''
    for c in cipher:
        if (c == ' '):
            msg += ' '
        else:
            c = ord(c)
            if (c <= ord('Z')) and (c>= ord('A')):
                c = (c - ord('A')  - key) % 26
                msg += chr(c + ord('A'))
            if (c <= ord('z')) and (c>= ord('a')):
                c = (c - ord('a')  - key) % 26
                msg += chr(c + ord('a'))
    return msg


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

nonce = get_random_bytes(16)

def establish_symm_keys(keylen):
    # generate a random key with given keylen
    kbyte = keylen // 8
    key = get_random_bytes(kbyte)
    return key


def enc_aes(plaintext,key):
    #AES encryption
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = plaintext.encode()
    cipher.update(plaintext)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def dec_aes(ciphertext, key):
    #AES decryption
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()


def symm_cipher():
    # main function for symmetric cipher
    # establish a pair of symmetric keys for Alice and Bob, Akey and Bkey
    Akey = establish_symm_keys(128)
    Bkey = Akey
    # Alice sends Bob a message
    A_msg = 'Hello Bob, what time should we meet?'
    ciphertext = enc_aes(A_msg, Akey)
    B_rec_msg = dec_aes(ciphertext, Bkey)
    print('Bob read message correctly?', B_rec_msg == A_msg)
    print('Bob reads:', B_rec_msg)

def caesar():
    # decrypt the caesar cipher below.
    plaintext = 'hello world'
    encrypted = caesar_enc(plaintext, 9)
    print(encrypted)
    cipher = 'H tlzzhnl myvt aol ltwlyvy'
    for k in range(0,26):
        msg = caesar_dec(cipher, k)
        print(k, msg)
    # look through the output above, a meaningful message in english is found, when k = 7. Thus, encryption key is 7.
    print(caesar_dec(cipher, 7))

caesar()
symm_cipher()
