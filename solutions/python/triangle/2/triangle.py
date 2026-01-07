"""Functions for determining triangle types: equilateral, isosceles, and scalene."""


def is_valid_triangle(sides):
    a, b, c = sides
    if a + b > c and a + c > b and b + c > a:
        return True
        
    else:
        return False


def equilateral(sides):
    a, b, c = sides
    if (a == b == c) and is_valid_triangle(sides):
        return True
        
    else:
        return False
        

def isosceles(sides):
    a, b, c = sides
    if (a == b or a == c or b == c) and is_valid_triangle(sides):
        return True
        
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if (a != b and b != c and a != c) and is_valid_triangle(sides):
        return True
        
    else:
        return False