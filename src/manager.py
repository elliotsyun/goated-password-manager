import random

# total encompassing list that stores all the types of password managers
MANAGER = []
SEEN_NAMES = set()


def create_group():
    '''Creates a storage object called a 'group' that has a dictionary
    for passwords and a purpose for the password'''

    name = input("Group Name: ")

    while True:

        if name in SEEN_NAMES:
            print(f"{name} is already an existing group, use another name.")
        else:
            print(f"{name} has been created and added to groups.")
            SEEN_NAMES.add(name)
            break

    # 2 item dictionary created with name, passwords, where passwords are {} its
    # own dictionary
    group = {"name": name, "passwords": {}}

    # total encompassing manager list that stores all types these password groups
    MANAGER.add(group)

    print(name, " has been created")
    print_manager()

    return group


def delete_group():  # need to make this

    return None


def print_manager():
    '''Prints the current password manager list'''
    print(MANAGER)
    return None


def add(group, id, new_pass):
    '''Adds a password to the password group'''

    if group not in MANAGER:
        print("This group does not exist.")
        return

    # create a new reference
    passwords = group[passwords]

    while True:

        # if it is a duplicate, tell them this id is already added
        if id in passwords:
            print(f"{id} is already in passwords, make a new id.")
        else:
            print(f"{id} is a unique id, commencing password addition")
            break

        # add key:value pair to passwords using pass_purpose:new_pass
    passwords[id] = new_pass

    # double check if it is added
    if (id, new_pass) in passwords:
        print(f"{id} has been added to {group}")
    else:
        print(f"There was an error in adding {id} to {group}")

    return group


def delete_pass(group, del_id):

    if group not in MANAGER:
        print("This group does not exist.")
        return

    passwords = group[passwords]

    # if the deletion id is not in passwords table, then print these
    if del_id not in passwords:
        print("The password identifier is not found or the password does not exist")
    else:
        print("Password identifier found, commencing deletion")

    # delete the password
    deleted = passwords.pop(del_id)

    # if it somehow is still in the passwords group
    if (del_id) in passwords:
        print(f"There was an error in deleting {del_id} from {group}")
    else:
        print(f"{del_id} with password {deleted} has been deleted from {group}")

    return group
