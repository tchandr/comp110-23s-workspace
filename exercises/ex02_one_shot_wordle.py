"""EX02 - One Shot Wordle."""

__author__ = "730564179"

secret_word: str = 'python'
word_input: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
char_val: int = 0


while len(word_input) != len(secret_word):
    word_input = input("That was not 6 letters! Try Again: ")

if len(word_input) == len(secret_word):
    while char_val < len(secret_word):
        if word_input[char_val] == secret_word[char_val]:
            emoji += GREEN_BOX
            char_val += 1
        else:
            check_letter: bool = False
            index: int = 0
            while check_letter is False and index < len(secret_word):
                if word_input[char_val] == secret_word[index]:
                    check_letter = True
                else:
                    index += 1
            if check_letter is True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX      
            char_val += 1
    if word_input == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite! Play again soon")
print(emoji)