"""Determine whether a number is an Armstrong number."""


def digit_count(number):
    """Return the number of digits in the given integer."""
    number = abs(number)
    if number == 0:
        return 1

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def armstrong_sum(number):
    """Return the sum of each digit raised to the power of the digit count."""
    power = digit_count(number)
    total = 0
    n = abs(number)

    while n > 0:
        total += (n % 10) ** power
        n //= 10
    return total
    
def is_armstrong_number(number):
    """Return True if the given number is an Armstrong number."""
    return armstrong_sum(number) == number
