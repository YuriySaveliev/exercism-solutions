def is_armstrong_number(number: int) -> bool:
    string_repr = str(number)
    return sum(
        int(digit) ** len(string_repr) 
        for digit in string_repr
    ) == number
