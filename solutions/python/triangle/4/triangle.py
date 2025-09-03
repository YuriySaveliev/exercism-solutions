def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) != 3 


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides):
    sum_all_sides = sum(sides)
    return sum_all_sides >= 2 * sides[2] and sum_all_sides >= 2 * sides[0] and sum_all_sides >= 2 * sides[1] and 0 not in sides
