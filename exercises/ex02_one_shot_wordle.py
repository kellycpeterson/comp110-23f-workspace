"""Game is similar to Wordle, but you have one guess"""
__author__: str = "730701948"

# word - guess
# secret - word to be guessed
word: str = input("What is your 6-letter guess? ")
secret: str = "python"
num_of_matches: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Repeat until len == 6
while(len(word)) != len(secret):
    word = input(f"That was not {len(secret)} letters! Try again:")

# put emojis in
emoji_count: str = ""
while num_of_matches <= len(secret) - 1:
    # if word at matches == secret at matches, add green
    if word[num_of_matches] == secret[num_of_matches]:
        emoji_count = emoji_count + GREEN_BOX
        num_of_matches = num_of_matches + 1
    else:
        in_word: bool = False
        secret_letters: int = 0
        # while not in secret and not reached end of secret
        while (in_word is not True) and (secret_letters <= len(secret) - 1):
            if secret[secret_letters] == word[num_of_matches]:
                in_word = True
            else:
                secret_letters = secret_letters + 1
        if (in_word is True):
            emoji_count = emoji_count + YELLOW_BOX
        else:
            emoji_count = emoji_count + WHITE_BOX
        num_of_matches = num_of_matches + 1

print(emoji_count)

if word != secret:
    print("Not quite. Play again soon!")    
else:
    print("Woo! You got it!")
