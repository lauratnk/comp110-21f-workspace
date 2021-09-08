"""Repeating a beat in a loop."""

__author__ = "730318786"


counter: int = 0
beat_name: str = input("What beat do you want to repeat? ")
beat_number: int = int(input("How many times do you want to repeat it? "))
beat_number_thingy: int = beat_number - 1
beat_name_thingy: str = beat_name + " "
beat_final: str = (beat_name_thingy * beat_number_thingy) + beat_name

if beat_number <= 0:
    print("No beat...")
else:
    print(beat_final)