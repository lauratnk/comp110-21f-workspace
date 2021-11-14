"""Project 1 Choose your own adventure."""

# Hi. I didn't finish.

__author__ = "730318786"

from random import randint

points: int = 0
player: str = ""
robot_head: str = "\U0001F916"

def main() -> None:
    """Starting point of the program."""
    greet()
    first_round()
    global player
    global points
    print(f"{robot_head} BEEP BOOP Welcome {player}! Now, let's begin! BOOP BEEP")
    print("The rules of the game are simple, I think of a number 1 through 10 and you have to guess it.")
    print("At the end of round one, you can...")
    print("1. Earn double or nothing by guessing Heads or Tails")
    print("2. Play The Number Game again")
    print("3. End the game")
    print("You have the possibility to earn 10 points each round. Each wrong guess takes a point away.")
    print("The higher the score, the better. BEEP BOOP")
    start_option: str = str(input(f"{robot_head} Would you like to begin? Yes or No?"))
    while start_option == "Yes":

 
def greet() -> None:
    """Greeting function."""
    print(f"{robot_head} BEEP BOOP Welcome to The Number Game.")
    global player
    player: str = str(input("What is your name, number guesser? BOOP BEEP"))
    print(f"Hello, {player}.")

def first_round() -> None:
    """Round function."""
    possible_points: int = 10
    first_number: int = randint(1, 10)
    first_number_str: str = str(first_number)
    guess: int = int(input(f"{robot_head} BEEP BOOP I thought of a number 1 through 10. What is your guess?"))
    while guess != first_number:
        possible_points = possible_points - 1 
        print("\U0001F916 WRONG!")
        guess: int = int(input(f"{robot_head} BEEP BOOP What is your new guess?"))
    print(f"\U0001F916 BEEP BOOP You are CORRECT! The number I was thinking of was {first_number_str}!")
    print(f"You earned a total of {possible_points} points this round!")
    global points
    points: int = points + possible_points
    print(f"That makes for a grand total of {points} points!")

def ending() -> None:
    """Offers an ending."""

if __name__ == "__main__":
    main()