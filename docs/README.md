# Password Manager Program

## Overview

This password manager program provides a baseline to interact with various functions created in different modules, including encryption, password generation, and password group management. It demonstrates the capabilities of managing and securing passwords through a command-line interface.

## Author
Elliot Yun

## Date
2024-06-18

## Version
1.0.1

## Features

- **Password Generation**: Generate passwords either randomly or based on given strings.
- **Password Management**: Create, search, and delete password groups and passwords within those groups.
- **AES Encryption**: Encrypt and decrypt passwords using AES encryption.

## Modules

### Main Module

This module provides the main interface for interacting with the password manager.

#### Example Usage

To run the main module, simply execute it:

```python
import encrypter
import manager
import generator

def main():
    # Interact with the password manager and demonstrate its capabilities
    # For detailed usage, refer to the example provided below in the main file

if __name__ == "__main__":
    main()
```

### Encryption Module

This module provides functions to encrypt and decrypt passwords using AES encryption.

#### Functions

- **encrypt(password)**: Encrypts a password using AES encryption.
- **decrypt(encryption)**: Decrypts an encrypted password.

#### Example Usage

To encrypt a password:

```python
result = encrypter.encrypt("my_password")
print(result)
```

To decrypt a password:

```python
original = encrypter.decrypt(result)
print(original)
```

### Generator Module

This module provides functions to generate passwords, either randomly or based on given keywords, and to return a user-provided password.

#### Functions

- **generate(length)**: Creates a random password of arbitrary length.
- **generate_with_string(input_string)**: Generates a password based on given keywords.
- **regular_password(password)**: Returns the password provided by the user.

#### Example Usage

To generate a random password:

```python
password = generator.generate(14)
print(password)
```

To generate a password based on keywords:

```python
password = generator.generate_with_string("example keyword")
print(password)
```

To return a user-provided password:

```python
password = generator.regular_password("user_password")
print(password)
```

### Manager Module

This module provides functions to manage password groups, including creating, searching, deleting groups, and adding, searching, deleting passwords within those groups.

#### Functions

- **print_manager()**: Prints the current password manager list.
- **create_group(group_name)**: Creates a storage object called a 'group' that has a dictionary for passwords and a purpose for the password.
- **search_group(group_name)**: Searches for a specific group in the manager.
- **delete_group(group_name)**: Deletes a specified group from the manager.
- **add_pass(group_name, id, new_pass)**: Adds a password to the password group.
- **search_id(group_name, id)**: Searches for a specific password id within a given group.
- **delete_pass(group_name, del_id)**: Deletes a password from a specific given group.

#### Example Usage

To create a new password group:

```python
manager.create_group("First")
```

To add a password to a group:

```python
manager.add_pass("First", "mypassword", "password_value")
```

To search for a password group:

```python
manager.search_group("First")
```

To delete a password from a group:

```python
manager.delete_pass("First", "mypassword")
```

## Running the Program

To run the main program and see the full demonstration of the password manager's capabilities, execute the `main` function in the main module.
The functions exist to be used however you want. The main file is just a demonstration of what you can do.

```bash
python main.py
```

This project is licensed under the MIT License.

```
The main program demonstrates how to generate, manage, and secure passwords. It integrates all the functionalities from the encryption, generator, and manager modules to provide a comprehensive password management solution. Enjoy managing your passwords securely!
```
