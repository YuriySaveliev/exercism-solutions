def is_armstrong_number(number):
    test_string = str(number)
    number_len = len(test_string)
    total = 0
    for item in test_string:
        total += int(item) ** number_len

    return total == number
        
