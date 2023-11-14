"""Evaluating sums three different ways."""
__author__: str = '730701948'

def w_sum(vals: list[float]) -> float: 
    """Using a while loop to find sum."""
    index: int = 0
    answer: float = 0.0
    while index < len(vals): 
        answer += vals[index]
        index += 1
    return answer    

def f_sum(vals: list[float]) -> float:
    """Using a for loop to find sum."""
    answer2: float = 0.0
    num: int = 0
    for num in vals:
        answer2+=num
    return answer2 

def f_range_sum(vals: list[float]) -> float:
    """Using a for range loops to find the sum."""
    answer3: float = 0.0
    num2: int = 0
    for num2 in range(0, len(vals)):
        answer3 += vals[num2]
    return answer3