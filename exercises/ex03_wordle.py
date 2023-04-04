"""EX03 - Structured Wordle."""


__author__ = "730564179"


def contains_char(input: str, char_input: str) -> bool:
    """Searches for character in string input."""
    check_letter: bool = False
    assert len(char_input) == 1
    index: int = 0
    while not check_letter and index < len(input):
        if input[index] == char_input:
            check_letter = True
            return check_letter
        index += 1
    return check_letter


def emojified(word_guess: str, secret: str) -> str:
    """Codified string output."""
    assert len(word_guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_string: str = ""
    index: int = 0
    while index < len(secret):
        if word_guess[index] == secret[index]:
            emoji_string += GREEN_BOX
            index += 1
        else:
            if contains_char(secret, word_guess[index]):
                emoji_string += YELLOW_BOX
                index += 1
            else:
                emoji_string += WHITE_BOX
                index += 1
    return emoji_string


def input_guess(input_num: int) -> str:
    """Checks integer value."""
    word_guess: str = input(f"Enter a {input_num} character word: ")
    while len(word_guess) != input_num:
        word_guess = input(f"That wasn't {input_num} chars! Try again: ")
    assert len(word_guess) == input_num
    return word_guess


def main() -> None:
    """Entrypoint for game."""
    turns: int = 1
    while (turns <= 6):
        print(f"===== Turn {turns}/6 =====")
        input: str = input_guess(5)
        print(emojified(input, "codes"))
        if input == "codes":
            return print(f"You won in {turns}/6 tries")
        turns += 1
    return print("X/6 - Sorry, try again tomorrow")


if __name__ == "__main__":
    main()