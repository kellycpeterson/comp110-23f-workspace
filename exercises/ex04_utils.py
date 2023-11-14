"""Practing lists."""
__author__: str = '730701948'

def all(list1: list[int], num1: int) -> bool:
    """Check if num1 = list[int]."""
    correct: bool = True
    index: int = 0
    while correct == True and index <= len(list1) - 1:
        if list1[index] == num1:
           index = index + 1
        else:
            correct = False
    return correct


def max(input: list[int]) -> int:
    """Checking for the max value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index2: int = 0
    maxvalue: int = input[0] 
    while index2 <= len(input) - 1:
        if maxvalue > input[index2]:
            index2 = index2 + 1
        else: 
            maxvalue = input[index2]
            index2 = index2 + 1
    return maxvalue


def is_equal(equal1: list[int], equal2: list[int]) -> bool: 
    """Checking if two lists have identical inputs."""
    index3: int = 0
    right: bool = True
    if len(equal1) != len(equal2):
        right = False
    while index3 <= len(equal1) and right == True:
        if equal1[index3] == equal2[index3]:
            index3 = index3 + 1
        else: 
            right = False
    return right