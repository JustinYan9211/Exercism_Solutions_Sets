"""Functions for determining whether a year is a leap year."""


def leap_year(year):
    """Return True if the given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False