'''
This module provides functions to encrypt and decrypt passwords using AES encryption.

Functions:
    encrypt(password): Encrypts a password using AES encryption.
    decrypt(encryption): Decrypts an encrypted password.

Example:
    To encrypt a password:

    >>> result = encrypt("my_password")
    >>> print(result)

    To decrypt a password:

    >>> original = decrypt(result)
    >>> print(original)

Author:
    Elliot Yun

Date:
    2024-06-04

Version:
    1.0.0
'''

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(password):
    '''
    Encrypts a password using AES encryption.

    Args:
        password (str): The password to encrypt.

    Returns:
        dict: A dictionary containing the encryption key, nonce, ciphertext, and authentication tag.
    '''

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
    '''
    Decrypts an encrypted password.

    Args:
        encryption(dict): A dictionary containing the encryption key, nonce, ciphertext, and authentication tag.

    Returns:
        str: The decrypted password.
    '''

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
