def caesar_enc(msg,key):
    # caesar cipher encryption function
    pass
    return cipher
def caesar_dec(cipher,key):
    # caesar cipher decryption function
    pass
    return msg


def establish_symm_keys(keylen):
    # generate a random key with given keylen
    pass
    return key


def enc_aes(plaintext,key):
    #AES encryption
    return ciphertext

def dec_aes(ciphertext, key):
    #AES decryption
    return plaintext


def symm_cipher():
    # main function for symmetric cipher
    # establish a pair of symmetric keys for Alice and Bob, Akey and Bkey
    # Alice sends Bob a message
    A_msg = 'Hello Bob, what time should we meet?'
    ciphertext = enc_aes(A_msg, Akey)
    B_rec_msg = dec_aes(ciphertext, Bkey)
    print('Bob read message correctly?', B_rec_msg == A_msg)

def caesar():
    # decrypt the caesar cipher below.
    cipher = 'H tlzzhnl myvt aol ltwlyvy'


#caesar()
#symm_cipher()