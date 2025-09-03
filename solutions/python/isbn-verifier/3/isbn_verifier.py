def is_valid(isbn: str) -> bool:
    cleared_isbn = isbn.split('-')
    cleared_isbn = ''.join(cleared_isbn)
    is_not_valid_isbn = len(cleared_isbn) != 10 or not cleared_isbn[:-1].isdigit() or (cleared_isbn[-1] != 'X' and cleared_isbn[-1].isalpha())
    if is_not_valid_isbn:
        return False
    
    elements_sum = 0
    for index, letter in enumerate(cleared_isbn):
        if index == 9 and letter == 'X':
            elements_sum += 10
            continue
        elements_sum += int(letter) * (10 - index)

    return elements_sum % 11 == 0
        