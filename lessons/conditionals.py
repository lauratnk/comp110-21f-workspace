"""An example of conditional if-else statements."""

SECRET: int = 3

print("I'm thinking of a number between one and five. What is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET:   
    print("You genius.")
    print("You wizard.")
    print("You guessed correctly!!!!!!!!")
else: 
    print("Wrong answer :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")
print("Game Over.")