"""
Purpose: To print the length of a word in list.
Auther: Roza Hadid
Date: 11.3.2024
"""


def str_len(lst: list):
    """
    Gets a variable of list type and print the length of all the words in it.
    :param lst: List that the function receive.
    """
    new_list = [len(member) for member in lst]
    print(new_list)
