#!/usr/bin/python3


def roman_to_int(roman_number: str) -> int:
    roman_correspondence = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    i = 0
    digital_number = 0
    length = len(roman_number)

    while i < length:
        if i + 1 < length and roman_number[i : i + 2] in roman_correspondence:
            digital_number += roman_correspondence[roman_number[i : i + 2]]
            i += 2
        else:
            digital_number += roman_correspondence[roman_number[i]]
            i += 1

    return digital_number
