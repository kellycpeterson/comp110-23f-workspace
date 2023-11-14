"""Creating dictionaries."""
__author__: str = '730701948'


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Values become keys and keys become values."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value encountered while inverting the dictionary")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finding the most popular favorite color."""
    color_counts = {}
    for color in color_dict.values():
        color_counts[color] = color_counts.get(color, 0) + 1
    max_count = max(color_counts.values())
    favorite_color = next(key for key, value in color_counts.items() if value == max_count)
    return favorite_color


def count(input_list: list[str]) -> dict[str, int]:
    """Count the number of times a value appears."""
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Sorting alphabetically."""
    alphabet_dict = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Tracking students' attendence."""
    if day in attendance_dict:
        if student in attendance_dict[day]:
            return attendance_dict
        else: 
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict