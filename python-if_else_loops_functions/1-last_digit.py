#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
print(
    f"""The last digit of {number} is {last_digit} and {
        "is greater than 5" if last_digit > 5 
       else ("is 0" if last_digit == 0 else "is less than 6 and not 0") }"""
)
