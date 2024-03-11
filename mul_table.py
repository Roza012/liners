"""
Purpose: Contains function that print a list of multiply numbers.
Auther: Roza Hadid
Date: 11.3.2024
"""


def mul_table(num: int):
    """
    Gets a number and multiply the numbers from 1 to the number that received by the variable himself.
    :param num: The number that the function gets.
    """
    new_lst = [num * i for i in range(1, 1 + num)]
    print(new_lst)