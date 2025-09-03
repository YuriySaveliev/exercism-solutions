def is_armstrong_number(number):
    test_string = str(number)
    number_len = len(test_string)
    total_sum = 0
    for item in test_string:
        total_sum += int(item) ** number_len

    return total_sum == number
        
