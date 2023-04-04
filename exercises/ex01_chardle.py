"""EX01 - Chardle - a cute step toward Wordle."""

__author__ = "730564179"


word_input: str = input("Enter a five letter word: ") 
if (len(word_input) != 5):
    print("Error: Word must contain 5 characters")
    exit() 
char_input: str = input("Enter your character: ")
if (len(char_input) != 1):
    print("Error: Character must be a single character")
    exit()
count: int = 0


print("Searching for " + char_input + " in " + word_input)

if (char_input == word_input[0]):
    print(char_input + " found at index 0")
    count += 1

if (char_input == word_input[1]):
    print(char_input + " found at index 1")
    count += 1

if (char_input == word_input[2]):
    print(char_input + " found at index 2")
    count += 1

if (char_input == word_input[3]):
    print(char_input + " found at index 3")
    count += 1

if (char_input == word_input[4]):
    print(char_input + " found at index 4")
    count += 1

if (count > 1):
    print(str(count) + " instances of " + char_input + " found in " + word_input)
elif (count == 1):
    print(str(count) + " instance of " + char_input + " found in " + word_input)
else:
    print("No instances of " + char_input + " found in " + word_input)
