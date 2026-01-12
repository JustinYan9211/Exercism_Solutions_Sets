"""Functions for calculating steps in the Collatz Conjecture."""


def steps(number):
    """Calculate Collatz steps to reach 1.

    :param number: int - starting positive integer.
    :return: int - number of transformation steps.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        count += 1
        
    return count 