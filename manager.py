import random

def create_storage():
    # create a dictionary and a new dictionary
    storage = {"id": [], "dict": {}, "keylist": []}
    print("This is your new storage with id", storage)
    return storage


def print_storage(dict):
    print(dict)
    return dict


def add(storage_object, encrypted_object):
    dict = storage_object["dict"]
    keylist = storage_object["keylist"]

    key = encrypted_object["key"]
    value = encrypted_object["ciphertext"]

    if value is None:
        print("Your password object has a key, but no value")

    dict.update(key, value)
    keylist.add()


def delete():
