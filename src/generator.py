import random
import string

'''
This module provides functions to generate passwords, either randomly or based on given keywords, and to return a user-provided password.

Functions:
    generate(length): Creates a random password of arbitrary length.
    generate_with_string(input_string): Generates a password based on given keywords, ensuring a minimum length.
    regular_password(password): Returns the password provided by the user.

Constants:
    DEFAULT_LENGTH (int): The default length for passwords.

Example:
    To generate a random password:

    >>> generate(14)

    To generate a password based on keywords:

    >>> generate_with_string("example keyword")

    To return a user-provided password:

    >>> regular_password("user_password")

Author:
    Elliot Yun

Date:
    2024-06-04

Version:
    1.0.0
'''

DEFAULT_LENGTH = 14


def generate(length):
    '''
    Creates a random password of arbitrary length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    '''

    characters = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(characters) for _ in range(length))

    print(result)

    return result


def generate_with_string(input_string):
    '''
    Generates a password based on given keywords, ensuring a minimum length of DEFAULT_LENGTH.

    Args:
        input_string (str): A string of keywords separated by whitespace.

    Returns:
        str: The generated password.
    '''

    # make keywords a string, make a list
    keywords = input_string.split()  # list
    result = ("".join(keywords)).replace(" ", "")  # string

    # if the string is less than DEFAULT_LENGTH, then add random characters to the end of it
    if len(result) < DEFAULT_LENGTH:  # 9

        remaining_length = DEFAULT_LENGTH - len(result)  # 5
        more_password = list(generate(remaining_length))  # list

        keywords += more_password  # concat the lists
        random.shuffle(keywords)
        result = "".join(keywords)

        return result

    else:
        random.shuffle(keywords)
        result = "".join(keywords)

    print(result)
    return result


def regular_password(password):
    '''
    Returns the password provided by the user.

    Args:
        password (str): The password to return.

    Returns:
        str: The provided password.
    '''
    reg_pass = str(password)

    print(reg_pass)
    return reg_pass
