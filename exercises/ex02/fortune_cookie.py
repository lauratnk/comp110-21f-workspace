"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730318786"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint

fortune_number: int = randint(1, 5)

print("Your fourtune cookie says....")


if fortune_number == 1:
    print("You will meet your soulmate in the next week")
else:
    if fortune_number == 2:
        print("Your past mistakes will catch up to you. Watch your back.")
    else:
        if fortune_number == 3:
            print("You will meet Charli XCX.")
        else:
            if fortune_number == 4:
                print("Your fave will follow you back on Twitter <3")
            else: 
                if fortune_number == 5:    
                    print("Call your mother.")


print("Have a wonderful day.")