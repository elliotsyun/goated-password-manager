import random
import string

DEFAULT_LENGTH = 14


def generate(length):
    '''Create a random password with arbitrary length'''

    characters = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(characters) for _ in range(length))

    print(result)

    return result


def identify_string(input_string):
    '''Separate an input string based on the types of characters within it'''

    digits = "".join([char for char in input_string if char.isdigit()])
    letters = "".join([char for char in input_string if char.isalpha()])
    punctuation = "".join(
        [char for char in input_string if char in string.punctuation])
    others = "".join(
        [char for char in input_string if not char.isdigit() and not char.isalpha() and char not in string.punctuation])

    return digits + letters + punctuation + others


def generate_with_string(keywords):
    '''Generate a string with given keywords, making sure that a string has at
    least a certain length of DEFAULT_LENGTH'''

    # make keywords a string
    password_string = identify_string(keywords)

    # make it a list so that we can shuffle it and give the result back as a string
    pass_list = list(password_string)
    random.shuffle(pass_list)
    result = "".join(pass_list)

    # if the string is less than DEFAULT_LENGTH, then add random characters to the end of it
    if len(password_string) < DEFAULT_LENGTH:  # 10
        remaining_length = DEFAULT_LENGTH - len(password_string)  # 4
        more_password = generate(remaining_length)  # generate 4 random
        result += more_password
        random.shuffle(result)

        print(result)
        return result

    print(result)
    return result


print("This is generate with string\n")
generate_with_string("abcdef1234!@#$;")

print("This is regular generate\n")
generate(DEFAULT_LENGTH)
