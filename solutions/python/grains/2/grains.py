"""Functions for calculating the number of grains on a chessboard."""


def is_valid_number(number):
    """Validate that the square number is between 1 and 64.

    :param number: int - square index on the chessboard.
    :raises ValueError: if number is not in the range 1–64.
    """
    
    if number < 1 or number >64:
        raise ValueError("square must be between 1 and 64")


def square(number):
    is_valid_number(number)
    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1
