from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

'''encrypt, decrypt passwords'''


def encrypt(password):
    '''Encrypts password using AES encryption'''

    # put the secret password into a byte literal
    data = bytes(password, "utf-8")
    print("This is the password", password)

    # generates a random 16 byte key
    key = get_random_bytes(16)
    print("This is the key", key)

    # creates a new AES cipher object using EAX mode
    cipher = AES.new(key, AES.MODE_EAX)
    print("This is the cipher", cipher)

    # creates encrypted data 'ciphertext' and creates authentication tag
    ciphertext, tag = cipher.encrypt_and_digest(data)
    print("This is ciphertext and tag", ciphertext, tag)

    # the number used once 'nonce'
    nonce = cipher.nonce
    print("This is nonce", nonce)

    # store result in dictionary
    result = {"key": key, "nonce": nonce, "ciphertext": ciphertext, "tag": tag}

    return result


def decrypt(encryption):
    '''Decrypts password'''

    # takes part of the encryption
    key = encryption["key"]
    nonce = encryption["nonce"]
    ciphertext = encryption["ciphertext"]
    tag = encryption["tag"]

    # creates the decryption cipher object with the same key and nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    print("This is the cipher again", cipher)

    # decrypts cipher back to original form with the tag
    data = cipher.decrypt_and_verify(ciphertext, tag)

    result = data.decode("utf-8")
    print("This is the result", result)

    return result


test = encrypt("Gon7P(}[`c?5hk")
decrypt(test)
