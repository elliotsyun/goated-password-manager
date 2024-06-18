"""
This module provides functions to manage password groups, including creating, searching, deleting groups, and adding, searching, deleting passwords within those groups.

Functions:
    print_manager(): Prints the current password manager list.
    create_group(group_name): Creates a storage object called a 'group' that has a dictionary for passwords and a purpose for the password.
    search_group(group_name): Searches for a specific group in the manager.
    delete_group(group_name): Deletes a specified group from the manager.
    add_pass(group_name, id, new_pass): Adds a password to the password group.
    search_id(group_name, id): Searches for a specific password id within a given group.
    delete_pass(group_name, del_id): Deletes a password from a specific given
    group.

Author:
    Elliot Yun

Date:
    2024-06-04

Version:
    1.0.1
"""

import random

# total encompassing list that stores all the types of password managers
MANAGER = {}
SEEN_NAMES = set()


def print_manager():
    """
    Prints the current password manager list.

    Returns:
        None
    """

    print("MANAGER -> GROUPS")
    for group_name in MANAGER:
        print(f"{group_name} ")
    return None


def create_group(group_name):
    """
    Creates a storage object called a 'group' that has a dictionary for passwords and a purpose for the password.

    Args:
        group_name (str): The name of the group to be created.

    Returns:
        tuple: The name and the group dictionary if created, otherwise None.
    """

    if group_name in SEEN_NAMES:
        print(
            f"The group, {group_name}, is already an existing group, use another name."
        )
        return None

    # create a 'group' where the name is the group name and the passwords is a dictionary of kvpairs
    group = {"name": group_name, "passwords": {}}

    # adds the group to the manager using group_name as the key
    MANAGER[group_name] = group
    SEEN_NAMES.add(group_name)

    print(f"The group, {group_name} has been created.")
    print_manager()

    return group_name, group


def search_group(group_name):
    """
    Searches for a specific group in the manager.

    Args:
        group_name (str): The name of the group to search for.

    Returns:
        bool: True if the group is found, otherwise False.
    """

    if group_name in MANAGER:
        print(f"The group, {group_name}, found.")
        return True
    else:
        print(f"The group, {group_name}, was not found.")
        return False


def delete_group(group_name):
    """
    Deletes a specified group from the manager.

    Args:
        group_name (str): The name of the group to delete.

    Returns:
        dict: The deleted group dictionary if deleted, otherwise None.
    """

    if group_name in MANAGER:
        deleted_group = MANAGER.pop(group_name)
        SEEN_NAMES.remove(group_name)
        print(f"The group, {group_name} has been deleted from your file MANAGER.")
        return deleted_group
    else:
        print("Group not found, halting deletion.")
        return None


def add_pass(group_name, id, new_pass):
    """
    Adds a password to the password group.

    Args:
        group_name (str): The name of the group.
        id (str): The id for the new password.
        new_pass (str): The password to be added.

    Returns:
        dict: The updated group dictionary if added, otherwise None.
    """

    if group_name not in MANAGER:
        print("This group does not exist.")
        return None

    group = MANAGER[group_name]
    passwords = group["passwords"]

    if id in passwords:
        print(f"{id} is already in passwords, make a new id.")
        return None

    passwords[id] = new_pass
    print(f"The id, {id}, has been added to the group, {group_name}.")
    return group


def search_id(group_name, id):
    """
    Searches for a specific password id within a given group.

    Args:
        group_name (str): The name of the group.
        id (str): The id of the password to search for.

    Returns:
        bool: True if the id is found, otherwise False.
    """

    if group_name not in MANAGER:
        print("This group does not exist.")
        return False

    group = MANAGER[group_name]
    passwords = group["passwords"]

    if id in passwords:
        print(f"The id, {id}, exists in the group, {group_name}")
        return True
    else:
        print(f"The id, {id}, does not exist or is not in this group.")
        return False


def delete_pass(group_name, del_id):
    """
    Deletes a password from a specific given group.

    Args:
        group_name (str): The name of the group.
        del_id (str): The id of the password to delete.

    Returns:
        tuple: The updated group dictionary and the deleted password if deleted,
        otherwise None.
    """

    if group_name not in MANAGER:
        print("This group does not exist.")
        return None

    group = MANAGER[group_name]
    passwords = group["passwords"]

    if del_id not in passwords:
        print("The password id is not found or the password does not exist.")
        return group, None
    else:
        deleted_pass = passwords.pop(del_id)
        print(
            f"The id, {del_id}, with password {deleted_pass} has been deleted from the group, {group_name}."
        )
        return group, deleted_pass
