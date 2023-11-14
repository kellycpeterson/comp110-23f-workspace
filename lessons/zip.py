"""Combining two lists into a dictionary"""
__author__: str = '730701948'

my_dict: dict[str, int] = dict()
def zip(word: list[str], numbers: list[int]) -> dict[str,int]:
    if len(word) != len(numbers):
        return dict()
    if len(word) == 0 or len(numbers) == 0:
        return dict()
    else:
        index: int = 0
        while index < len(word):
            my_dict[word[index]] = numbers[index]
            index = index + 1
    return my_dict