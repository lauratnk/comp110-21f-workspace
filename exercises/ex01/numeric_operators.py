"""This is the code for EX01 numeric operator portion."""

__author__ = "730318786"

left_hand_side_str: str = input("Left-hand side: ")
right_hand_side_str: str = input("Right-hand side: ")
left_hand_side_int: int = int(left_hand_side_str)
right_hand_side_int: int = int(right_hand_side_str)

first_eval: str = str(left_hand_side_int ** right_hand_side_int)
print(left_hand_side_str + " ** " + right_hand_side_str + " is " + first_eval)
second_eval: str = str(left_hand_side_int / right_hand_side_int)
print(left_hand_side_str + " / " + right_hand_side_str + " is " + second_eval)
third_eval: str = str(left_hand_side_int // right_hand_side_int)
print(left_hand_side_str + " // " + right_hand_side_str + " is " + third_eval)
fourth_eval: str = str(left_hand_side_int % right_hand_side_int)
print(left_hand_side_str + " % " + right_hand_side_str + " is " + fourth_eval)