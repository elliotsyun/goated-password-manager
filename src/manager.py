import random

# total encompassing list that stores all the types of password managers
MANAGER = {}
SEEN_NAMES = set()


def print_manager():
    '''Prints the current password manager list'''
    print("Current Groups in Manager:")
    for group_name in MANAGER:
        print(f"{group_name} ")
    return None


def create_group(group_name):
    '''Creates a storage object called a 'group' that has a dictionary
    for passwords and a purpose for the password'''

    if group_name in SEEN_NAMES:
        print(f"{group_name} is already an existing group, use another name.")
        return None

    # 2 item dictionary created with name, passwords, where passwords are {} its
    # own dictionary

    group = {"name": group_name, "passwords": {}}

    # adds the group to the manager using group_name as the key
    MANAGER[group_name] = group

    print(group_name, " has been created")
    print_manager()

    return group


def search_group(group_name):
    '''Searches for a specific group in the manager'''

    if group_name in MANAGER:
        print(f"{group_name} found")
        return MANAGER[group_name]
    else:
        print(f"{group_name} not found")
        return None


def delete_group(group_name):

    # the group name exists and group is in manager

    # the group is deleted

    # the group is returned

    return None


def add_pass(group_name, id, new_pass):
    '''Adds a password to the password group'''

    if group not in MANAGER:
        print("This group does not exist.")
        return

    # create a new reference
    group = MANAGER[group_name]
    passwords = group[passwords]

    while True:

        # if it is a duplicate, tell them this id is already added
        if id in passwords:
            print(f"{id} is already in passwords, make a new id.")
        else:
            print(f"{id} is a unique id, commencing password addition...")
            break

        # add key:value pair to passwords using id:new_pass
    passwords[id] = new_pass

    # double check if it is added
    if (id, new_pass) in passwords:
        print(f"{id} has been added to {group_name}")
    else:
        print(f"There was an error in adding {id} to {group_name}")

    return group


def delete_pass(group_name, del_id):

    if group not in MANAGER:
        print("This group does not exist.")
        return

    group = MANAGER[group_name]
    passwords = group[passwords]

    # if the deletion id is not in passwords table, then print these
    if del_id not in passwords:
        print("The password identifier is not found or the password does not exist")
        return group
    else:
        print("Password identifier found, commencing deletion...")

    # delete the password
    deleted_pass = passwords.pop(del_id)

    # if it somehow is still in the passwords group
    if (del_id) in passwords:
        print(f"There was an error in deleting {del_id} from {group_name}")
    else:
        print(
            f"{del_id} with password {deleted_pass} has been deleted from {group_name}")

    return group, deleted_pass
