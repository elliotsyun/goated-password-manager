"""
This module provides a baseline to interact with all my functions created in my other modules

Author:
    Elliot Yun

Date:
    2024-06-18

Version:
    1.0.1
"""

import encrypter
import manager
import generator


"""welcome to the main file
the objective of this file is to simply demonstrate the capabilities of my password manager
"""


def main():

    # Create a password manager with all the groups

    print("This is the current manager and its groups:", manager.print_manager())

    # Then go into generating a password

    while True:
        pass_response = (
            input(
                "Would you like to generate a password or write your own? (generate/write/g/w) "
            )
            .strip()
            .lower()
        )

        if pass_response not in ["g", "w", "generate", "write"]:
            print(
                "Sorry, I didn't understand that, please rewrite if you want to generate or write your own password."
            )

        else:
            if pass_response in ["g", "generate"]:
                while True:
                    gen_method = (
                        input(
                            "Do you want to generate a password randomly or with given strings? (random/strings/r/s) "
                        )
                        .strip()
                        .lower()
                    )

                    if gen_method not in ["random", "strings", "r", "s"]:
                        print(
                            "Sorry, please rewrite which way you want to generate your password."
                        )

                    else:
                        if gen_method in ["random", "r"]:
                            print("You chose to randomly generate your password.")
                            pass_length = int(
                                input(
                                    "Please input your desired length for your password: "
                                )
                            )
                            password = generator.generate(pass_length)
                            print(
                                "This is your password (this will be discrete in implementation): ",
                                password,
                            )
                            break
                        elif gen_method in ["strings", "s"]:
                            print(
                                "You chose to generate your password with input strings."
                            )
                            pass_strings = input(
                                "Please write your input strings, separated by white spaces: "
                            )
                            password = generator.generate_with_string(pass_strings)
                            print(
                                "This is your password (this will be discrete in implementation): ",
                                password,
                            )

                        break

            elif pass_response in ["write", "w"]:
                print("You chose to write your password.")
                pass_regular = input("Please write your password: ")
                password = generator.regular_password(pass_regular)
                print(
                    "This is your password (this will be discrete in implementation): ",
                    password,
                )
                break
        break

    # Encrypt the password using AES and show the encryption

    # Create a password group

    # Add the password to a specific group and print it out

    return None


main()
