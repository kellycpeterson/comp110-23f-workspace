"""Test my zip function."""
__author__: str = '730701948'

from lessons.zip import zip 

def test1_empty_list():
    """Testing for empty dictionary."""
    list1 = []
    list2 = []
    assert zip(list1, list2) == {}


def test2_user_test():
    """Testing for two inputs."""
    list3 = ["red", "orange"]
    list4 = [1,2]
    assert zip(list3, list4) == {"red": 1, "orange": 2}


def test3_user_test(): 
    """Testing for four inputs."""
    list5 = ["cars", "sharks", "horses", "frog"]
    list6 = [1, 2, 3, 4]
    assert zip(list5, list6) == {"cars": 1, "sharks": 2, "horses": 3, "frog": 4}