def is_armstrong_number(number):
    test_string = str(number)
    number_len = len(test_string)
    total = 0
    total = sum(int(digit) ** number_len for digit in test_string)
    return total == number
