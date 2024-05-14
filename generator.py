import random
import string

DEFAULT_LENGTH = 14


def generate(length):
    '''Create a random password with arbitrary length'''

    characters = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(characters) for _ in range(length))

    print(result)

    return result


def generate_with_string(input_string):
    '''Generate a string with given keywords, separated by whitespace, making sure that a string has at
    least a certain length of DEFAULT_LENGTH'''

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
    reg_pass = str(password)

    print(reg_pass)
    return reg_pass


print("This is generate with string")
generate_with_string("pen is esss hai rs")
print("\n")

print("This is regular generate")
generate(DEFAULT_LENGTH)
print("\n")

print("This is the regular no generate password")
regular_password("penis hair")
