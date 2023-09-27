"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730701948"

word = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: word must contain 5 characters")
    exit()
letter = input("Enter a single character:")
if len(letter) != 1:
    print("Error: character must be a single character")
    exit()
print("Searching for " + letter + " in " + word)
num_of_matches = 0
if word[0] == letter:
    print(letter + " found at index 0")
    num_of_matches = num_of_matches + 1
if word[1] == letter: 
    print(letter + " found at index 1")
    num_of_matches = num_of_matches + 1
if word[2] == letter:
    print(letter + " found at index 2")
    num_of_matches = num_of_matches + 1
if word[3] == letter:
    print(letter + " found at index 3")
    num_of_matches = num_of_matches + 1
if word[4] == letter:
    print(letter + " found at index 4")
    num_of_matches = num_of_matches + 1
if num_of_matches > 1: 
    print(str(num_of_matches) + " instances of " + letter + " found in " + word)
if num_of_matches == 1:
    print("1 instance of " + letter + " found in " + word)
if num_of_matches == 0: 
    print("No instances of " + letter + " found in " + word)
