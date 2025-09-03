def is_armstrong_number(number):
    test_string = str(number)
    number_len = len(test_string)
    return sum(int(digit) ** number_len for digit in test_string) == number
