"""Unit testing my functions."""
__author__: str = '730701948'

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_1_empty_dict1():
    """Testing for empty dictionary."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_2_user_test2():
    """Testing for dictionary inputs."""
    dict1: dict[str, str] = {"red": "apple", "yellow": "lemon"}
    assert invert(dict1) == {"apple": "red", "lemon": "yellow"} 


def test_3_user_test3():
    """Testing for more dictionary inputs."""
    dict1: dict[str, str] = {"summer": "hot", "fall": "cool", "winter": "cold"}
    assert invert(dict1) == {"hot": "summer", "cool": "fall", "cold": "winter"}


def test_1_empty_dict4():
    """Testing for empty dictionary."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {} 


def test_2_user_test5():
    """Testing for popular color dictionary inputs."""
    dict1: dict[str, str] = {"Nate": "blue"}
    assert favorite_color(dict1) == "blue"


def test_3_user_test6(): 
    """Testing for medium popular dictionary inputs."""
    dict1: dict[str, str] = {"Sam": "red", "Helen": "pink", "Brad": "green"}
    assert favorite_color(dict1) == "red"


def test_1_empty_list7():
    """Testing for empty list."""
    list1: list[str] = []
    assert count(list1) == {}


def test_2_user_test9():
    """Testing for correct counting."""
    list2: list[str] = ["1", "1", "1", "2", "3", "3"]
    assert count(list2) == {"1": 3, "2": 1, "3": 2}


def test_3_user_test10():
    """Testing for proper dictionary count."""
    list3 = {"red", "orange", "red"}
    assert count(list3) == {"red": 2, "orange": 1}


def test_1_empty_list11(): 
    """Testing for empty list."""
    list1: list[str] = []
    assert alphabetizer(list1) == {}


def test_2_user_test12():
    """Testing alphabetical categories."""
    list2: list[str] = ["act", "apple", "cat", "camera"]
    assert alphabetizer(list2) == {"a": ["act", "apple"], "c": ["cat", "camera"]}


def test_3_user_test13():
    """Test similar sounding words."""
    list3: list[str] = ["fish", "photo", "phew", "fine"]
    assert alphabetizer(list3) == {"f": ["fish", "fine"], "p": ["photo", "phew"]}


def test_1_empty_dict14():
    """Testing for empty dictionary."""
    day: str = ""
    students: list = []
    dict1: dict[str, list[str]] = {}
    assert update_attendance(dict1, day, students) == {}


def test_2_user_test15():
    """Testing for Tuesday attendence."""
    day: str = "Tuesday"
    students: list = ["Anna", "Mal", "Hannah"]
    dict2: dict[str, list[str]] = {"Tuesday": ["Ryan"]}
    assert update_attendance(dict2, day, students) == {"Tuesday": ["Ryan", "Anna", "Mal", "Hannah"]}


def test_3_user_test16():
    """Testing for weekend attendence."""
    day: str = "Saturday"
    students: list = ["None"]
    dict3: dict[str, list[str]] = {"Saturday": ["None"]}
    assert update_attendance(dict3, day, students) == {"Saturday": ["None"]}