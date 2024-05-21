from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(password):
    """Encrypts password using AES encryption"""

    # put the secret password into a byte literal
    data = bytes(password)
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

    return key, nonce, ciphertext, tag


def decrypt(ciphertext, key, tag, nonce):
    """Decrypts password"""

    # creates the decryption cipher object with the same key and nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce)

    # decrypts cipher back to original form
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data
