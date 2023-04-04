"""EX06 - Choose your own adventure."""

__author__ = "730564179"

from random import randint

player: str
points: int = 1000
tutpoints: int
DICE_ONE: str = "\u2680"
DICE_TWO: str = "\u2681"
DICE_THREE: str = "\u2682"
DICE_FOUR: str = "\u2683"
DICE_FIVE: str = "\u2684"
DICE_SIX: str = "\u2685"
dice_dict: dict[int, str] = {1: DICE_ONE, 2: DICE_TWO, 3: DICE_THREE, 4: DICE_FOUR, 5: DICE_FIVE, 6: DICE_SIX}
bet_dict: dict[int, float] = {4: 1.3, 5: 1.27, 6: 1.25, 8: 1.25, 9: 1.27, 10: 1.3, 11: 1.35}


def main() -> None:
    """Main Function."""
    global points
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    greet()
    print(" ")
    print("You now have three options. Type 1 if you want to play the real game and gamble. This will affect your total points")
    print("Type 2 if you want to enter a tutorial. Your points won't be added or subtracted in this game mode")
    print("Type 3 is you want to quit, which will end the game.")
    print(f"You have {points} points")
    options: int = int(input("Enter your option: "))
    while points >= 10:
        if options == 1:
            game(points)
        elif options == 2:
            tutorial()
        elif options == 3:
            goodbye()
        else:
            game(points)
    points = game(points)
    goodbye()


def greet() -> None:
    """Greets player."""
    global player
    player = input("Enter your name: ")
    print(f"Welcome to Hazard {player}! A two-dice guessing and gambling game.")
    print("You will soon be prompted to choose a wager amount up to 100 points and a minimum bet of 10. You have 1000 points to spend")
    print("You are given the chance to roll 2 dice. If the two dice sums to a 7 or 11, you win your wager with a payout of 1:2.2")
    print("If you roll a 2, 3, or 12, you automatically lose")
    print("If you roll a sum of anything else, you enter a second round, where you have to match the sum of the first round. This sum is called a main.")
    print("In the second round, you'll have the option to wager again after each chance")
    print("Rolling a 7 means you automatically lose. Rolling the main means you win your payout. The payout is dependent on the value of the main")
    print("A main of 6 or 8 is a payout of 1:2.5, 5 or 9 is a payout of 1:2.7, 4 or 10 is a payout of 1:3, and 11 is a payout of 1:3.5")
    print("You will keep rolling until you hit the main, or hit a 7")
    print("A payout means your rewarded with the product of your wager. For example a wager of 50 points with a payout of 1:2.5 will award you 125 points")


def tutorial() -> None:
    """Tutorial version."""
    global points
    global player
    global tutpoints
    tutpoints = 1000
    wager: int = int(input("Enter your wager: "))
    while wager > 100:
        print("Wager has to be less than 100")
        wager = int(input("Enter your wager: "))
    while wager < 10:
        print("Wager has to be more than 10 points")
        wager = int(input("Enter your wager: "))
    while wager > tutpoints:
        print("Wager is more than your total points")
        wager = int(input("Enter your wager: "))
    tutpoints -= wager
    sum: int = tutroll()
    if sum == 2 or sum == 3 or sum == 12:
        print(f"You lost your wager. Your total points is now: {tutpoints}. Better luck next time {player}")
        tutpoints = 1000
        main()
    elif sum == 7 or sum == 11:
        tutpoints += int(wager * 2.2)
        print(f"You won the first round. Your total is now {tutpoints}. Good job {player}!")
        tutpoints = 1000
        main()
    else:
        newsum: int = 0
        while newsum != 7:
            print(f"The main is now {sum}, the loss is 7")
            newwager = int(input("Enter a wager amount: "))
            while newwager > 100:
                print("Wager has to be less than 100")
                newwager = int(input("Enter your wager: "))
            while newwager < 10:
                print("Wager has to be more than 10 points")
                newwager = int(input("Enter your wager: "))
            while newwager + wager > tutpoints:
                print("Wager is more than your points")
                newwager = int(input("Enter your wager: "))
            wager += newwager
            tutpoints -= newwager
            newsum = tutroll()
            if newsum == sum:
                tutpoints += int(wager * (bet_dict[newsum]))
                print(f"You won, your total points is {tutpoints}, good job {player}!")
                main()
                tutpoints = 1000
        print(f"You lost, your total points is {tutpoints}, better luck next time {player}!")
        tutpoints = 1000
        main()


def game(point: int) -> int:
    """Gambling game."""
    global points
    global player
    point = points
    wager: int = int(input("Enter your wager: "))
    while wager > 100:
        print("Wager has to be less than 100")
        wager = int(input("Enter your wager: "))
    while wager < 10:
        print("Wager has to be more than 10 points")
        wager = int(input("Enter your wager: "))
    while wager > point:
        print("Wager is more than your total points")
        wager = int(input("Enter your wager: "))
    points -= wager
    sum: int = roll()
    if sum == 2 or sum == 3 or sum == 12:
        print(f"You lost your wager. Your total points is now: {points}, better luck next time {player}")
        main()
        return points
    elif sum == 7 or sum == 11:
        points += int(wager * 2.2)
        print(f"You won the first round. Your total is now {points}, good job {player}!")
        main()
        return points
    else:
        newsum: int = 0
        while newsum != 7:
            print(f"The main is now {sum}, the loss is 7")
            newwager = int(input("Enter a wager amount: "))
            while newwager > 100:
                print("Wager has to be less than 100")
                newwager = int(input("Enter your wager: "))
            while newwager < 10:
                print("Wager has to be more than 10 points")
                newwager = int(input("Enter your wager: "))
            while newwager + wager > points:
                print("Wager is more than your points")
                newwager = int(input("Enter your wager: "))
            wager += newwager
            points -= newwager
            newsum = roll()
            if newsum == sum:
                points += int(wager * (bet_dict[newsum]))
                print(f"You won, your total points is {points}, good job {player}")
                main()
                return points
        print(f"You lost, your total points is {points}, better luck next time {player}")
        main()
        return points


def roll() -> int:
    """Roll function."""
    global points
    dice1: int = randint(1, 6)
    dice2: int = randint(1, 6)
    sum: int = dice1 + dice2
    print(f"Dice 1: {dice1}, Dice 2: {dice2}, You rolled a {sum}, Total points: {points}")
    print(dice_dict[dice1] + " " + dice_dict[dice2])
    return sum


def tutroll() -> int:
    """Roll function."""
    global tutpoints
    dice1: int = randint(1, 6)
    dice2: int = randint(1, 6)
    sum: int = dice1 + dice2
    print(f"Dice 1: {dice1}, Dice 2: {dice2}, You rolled a {sum}, Total points: {tutpoints}")
    print(dice_dict[dice1] + " " + dice_dict[dice2])
    return sum


def goodbye() -> None:
    """Goodbye function."""
    global player
    global points
    print(f"Here's how many points you made {player}: {points}")
    print("Goodbye")
    quit()


if __name__ == "__main__":
    main()