import random

'''print_manager, create_group, search_group, delete_group, add_pass, search_id,
delete_pass'''

# total encompassing list that stores all the types of password managers
MANAGER = {}
SEEN_NAMES = set()


def print_manager():
    '''Prints the current password manager list'''

    print("MANAGER -> GROUPS")
    for group_name in MANAGER:
        print(f"{group_name} ")
    return None


def create_group(group_name):
    '''Creates a storage object called a 'group' that has a dictionary
    for passwords and a purpose for the password'''

    # search for the group_name in SEEN_NAMES

    if group_name in SEEN_NAMES:
        print(
            f"The group, {group_name}, is already an existing group, use another name.")
        return None

    # create a 'group' where the name is the group name and the passwords is a
    # dictionary of kvpairs

    group = {"name": group_name, "passwords": {}}

    # adds the group to the manager using group_name as the key
    MANAGER[group_name] = group

    if (group_name, group) in MANAGER:
        print(f"The group, {group_name} has been created.")
        return group_name, group
    else:
        print(f"There was an error in creating the group, {group_name}.")

    print(group_name, " has been created")
    print_manager()

    return group_name, group


def search_group(group_name):
    '''Searches for a specific group in the manager'''

    if group_name in MANAGER:
        print(f"The group, {group_name}, found.")
        return True
    else:
        print(f"The group, {group_name}, was not found.")
        return False


def delete_group(group_name):

    if search_group(group_name):
        print("Commencing deletion...")
    else:
        print("Group not found, halting deletion.")

    deleted_group = MANAGER.pop(group_name)

    # double check if it isn't deleted

    if (group_name) in MANAGER:
        print(
            f"There was an error in deleting the group, {deleted_group}, from your file MANAGER.")
    else:
        print(
            f"The group, {group_name} has been deleted from your file MANAGER.")

    return deleted_group


def add_pass(group_name, id, new_pass):
    '''Adds a password to the password group'''

    if group_name not in MANAGER:
        print("This group does not exist.")
        return

    # create a new reference
    group = MANAGER[group_name]
    passwords = group[passwords]

    while True:

        # if it is a duplicate, say this id is already added
        if id in passwords:
            print(f"{id} is already in passwords, make a new id.")
        else:
            print(f"{id} is a unique id, commencing password addition...")
            break

        # add kv pair to passwords using id:new_pass
    passwords[id] = new_pass

    # double check if it is added
    if (id, new_pass) in passwords:
        print(f"The id, {id}, has been added to the group, {group_name}.")
    else:
        print(
            f"There was an error in adding id, {id}, to the group, {group_name}.")

    return group


def search_id(group_name, id):

    if group_name not in MANAGER:
        print("This group does not exist.")
        return

    group = MANAGER[group_name]
    passwords = group[passwords]

    if id in passwords:
        print(f"The id, {id}, exists in the group, {group_name}")
        return True
    else:
        print(f"The id, {id}, does not exist or is not in this group.")
        return False


def delete_pass(group_name, del_id):
    '''Deletes a password from a specific given group'''

    if group_name not in MANAGER:
        print("This group does not exist.")
        return

    group = MANAGER[group_name]
    passwords = group[passwords]

    # if the deletion id is not in passwords table, then print these
    if del_id not in passwords:
        print("The password id is not found or the password does not exist.")
        return group
    else:
        print("Password id found, commencing deletion...")

    # delete the password
    deleted_pass = passwords.pop(del_id)

    # double check if it is deleted
    if (del_id) in passwords:
        print(
            f"There was an error in deleting the id, {del_id}, from the group, {group_name}.")
    else:
        print(
            f"The id, {del_id}, with password {deleted_pass} has been deleted from the group, {group_name}.")

    return group, deleted_pass
