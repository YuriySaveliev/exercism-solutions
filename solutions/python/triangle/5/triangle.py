def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) != 3 


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides):
    sum_all_sides = sum(sides)
    return all(sum_all_sides >= 2 * side for side in sides) and 0 not in sides
