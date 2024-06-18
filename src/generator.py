import random
import string

"""
This module provides functions to generate passwords, either randomly or based on given keywords, and to return a user-provided password.

Functions:
    generate(length): Creates a random password of arbitrary length.
    generate_with_string(input_string): Generates a password based on given keywords.
    regular_password(password): Returns the password provided by the user.

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
    2024-06-18

Version:
    1.0.1
"""


def generate(length):
    """
    Creates a random password of arbitrary length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(characters) for _ in range(length))

    return result


def generate_with_string(input_string, seed=None):
    """
    Generates a password based on given keywords, and mixes in a random amount of characters.

    Args:
        input_string (str): A string of keywords separated by whitespace.
        seed (int, optional): Seed for random generator to ensure reproducibility. Defaults to None.

    Returns:
        str: The generated password.
    """
    if seed is not None:
        random.seed(seed)

    keywords = input_string.split()
    joined_keywords = "".join(keywords)

    random_num = random.randint(3, 11)
    random_chars = list(generate(random_num))

    if not any(char.isdigit() for char in joined_keywords):
        random_chars.append(random.choice(string.digits))
    if not any(char in string.punctuation for char in joined_keywords):
        random_chars.append(random.choice(string.punctuation))

    random.shuffle(random_chars)

    # Insert the keywords into the shuffled random characters
    insertion_index = random.randint(0, len(random_chars))
    password_chars = (
        random_chars[:insertion_index]
        + [joined_keywords]
        + random_chars[insertion_index:]
    )

    result = "".join(password_chars)
    return result


def regular_password(password):
    """
    Returns the password provided by the user.

    Args:
        password (str): The password to return.

    Returns:
        str: The provided password.
    """
    reg_pass = str(password)

    return reg_pass
