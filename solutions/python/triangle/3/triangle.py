"""Functions for determining triangle types: equilateral, isosceles, and scalene."""


def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a


def equilateral(sides):
    a, b, c = sides
    return (a == b == c) and is_valid_triangle(sides)
        

def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and is_valid_triangle(sides)



def scalene(sides):
    a, b, c = sides
    return (a != b and b != c and a != c) and is_valid_triangle(sides)