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
    items_sum = sum(digit for digit in range(1, number) if number % digit == 0)
    if items_sum == number:
        return TypeOfNumber.PERFECT.value
    elif items_sum > number:
        return TypeOfNumber.ABUNDANT.value
    return TypeOfNumber.DEFICIENT.value
