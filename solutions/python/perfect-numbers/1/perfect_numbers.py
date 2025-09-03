from enum import Enum


class TypeOfNumber(Enum):
    ABUNDANT = 'abundant'
    PERFECT = 'perfect'
    DEFICIENT = 'deficient'

    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    items = []
    for digit in range(1, number):
        if number % digit == 0:
            items.append(digit)
    if sum(items) == number:
        return TypeOfNumber.PERFECT.value
    elif sum(items) > number:
        return TypeOfNumber.ABUNDANT.value
    return TypeOfNumber.DEFICIENT.value
