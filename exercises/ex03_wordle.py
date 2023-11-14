"""Game is similar to Wordle, but you have one guess."""
__author__: str = '730701948'

# word - guess
# secret - word to be guessed

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# def fun_name(var: int)-> return_type:
def contains_char(word: str, letter: str) -> bool:
    """Finds a letter in a word."""
    assert len(letter) == 1
    in_word: bool = False
    secret_letters: int = 0
    # while not in secret and not reached end of secret 
    while (in_word is not True) and (secret_letters <= len(word) - 1):
        if word[secret_letters] == letter:
            in_word = True
        else:
            secret_letters = secret_letters + 1
    return in_word


# Repeat until len == 6
def input_guess(length: int) -> str:
    """Input guess and have it checked.""" 
    word: str = input(f"Enter a {length} character word: ")
    while len(word) != length:
        word = input(f"That wasn't {length} chars! Try again: ")
    return word


# put emojis in
def emojified(word: str, secret: str) -> str:
    """Add boxes.""" 
    assert len(word) == len(secret)
    index: int = 0
    emoji_list: str = ""
    while index <= len(secret) - 1:
        if word[index] == secret[index]:
            emoji_list += GREEN_BOX 
        elif contains_char(secret, word[index]):
            emoji_list += YELLOW_BOX
        elif contains_char(secret, word[index]) is False:
            emoji_list += WHITE_BOX
        index += 1
    return emoji_list  


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    counter: int = 1 
    length: int = len(secret)
    word: str = ""
    while (!= secret and counter <= 6): 
        print(f"=== Turn {counter}/6 ===")
        word = input_guess(length)
        print(emojified(word, secret))
        counter += 1
    if word == secret:
        print(f"You won in {counter-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__": 