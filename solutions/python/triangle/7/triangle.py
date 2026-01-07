"""Functions for determining triangle types: equilateral, isosceles, and scalene."""


def is_valid_triangle(sides: list[int]) -> bool:
    """Return True if sides form a valid triangle."""
    
    if len(sides) != 3:
        return False
    
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a

    
def equilateral(sides: list[int]) -> bool:
    a, b, c = sides
    return (a == b == c) and is_valid_triangle(sides)
        

def isosceles(sides: list[int]) -> bool:
    a, b, c = sides
    return (a == b or a == c or b == c) and is_valid_triangle(sides)


def scalene(sides: list[int]) -> bool:
    a, b, c = sides
    return (a != b and b != c and a != c) and is_valid_triangle(sides)