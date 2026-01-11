"""Determine whether a number is an Armstrong number."""


def is_armstrong_number(number):
    digits = str(abs(number))
    power = len(digits)

    total = 0
    for d in digits:
        total += int(d) ** power

    return total == abs(number)