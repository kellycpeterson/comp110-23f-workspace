"""Game is similar to Wordle, but you have one guess."""
__author__: str = "730701948"

# word - guess
# secret - word to be guessed

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# def fun_name(var: int)-> return_type:
def contains_char(word: str, letter: str) -> bool:
    """Finds a letter in a word."""
    assert len (letter) == 1
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
    word: str = input(f"What is your {length}-letter guess? ")
    while len(word) != length:
        word = input(f"That was not {length} letters! Try again:")
    return word


# put emojis in
def emojified(word: str, secret: str) -> str:
    """Add boxes.""" 
    assert len(word) == len(secret)
    num_of_matches: int = 0
    emoji_count: str = ""
    while num_of_matches <= len(secret) - 1:
        if word[num_of_matches] == secret[num_of_matches]:
            emoji_count = emoji_count + GREEN_BOX
            num_of_matches = num_of_matches + 1
        else:
            secret_letters: int = 0
            if (contains_char(secret, word[secret_letters]) is True):
                emoji_count = emoji_count + YELLOW_BOX
            else:
                emoji_count = emoji_count + WHITE_BOX
            num_of_matches = num_of_matches + 1
    return emoji_count 


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    step_1: str = input_guess(len(secret))
    step_2: int = 1
    while (step_1 != secret and step_2 < 6): 
        step_1 = input_guess(len(secret))
        print(emojified(step_1, secret))
        step_2 = step_2 + 1
    
    if secret == step_1:
        print(f"You won in {step_2}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")