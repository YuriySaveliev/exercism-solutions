def square_of_sum(number):
    square_sum = 0
    for item in range(1, number + 1):
        square_sum += item
    return square_sum ** 2


def sum_of_squares(number):
    sum_square = 0
    for item in range(1, number + 1):
        sum_square += item ** 2
    return sum_square


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
