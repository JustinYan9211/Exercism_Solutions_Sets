"""Functions for determining whether a year is a leap year."""


def leap_year(year: int) -> bool:
    """Return True if the given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0