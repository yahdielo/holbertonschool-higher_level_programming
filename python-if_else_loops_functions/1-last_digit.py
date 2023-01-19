#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num_str = repr(number)

last_digit = num_str[-1]

if number < 0:
    sign = "-"
    print(f"Last digit if {number} is {sign}{last_digit} and is less than 6 and not 0")
else:

    if last_digit == "0":
        print(f"Last digit of {number} is 0 and is {last_digit}")

    elif last_digit > "5":
        print(f"Last digit of {number} is {last_digit} and is greater than 5")

    elif last_digit < "6" and last_digit > "0":
        print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

