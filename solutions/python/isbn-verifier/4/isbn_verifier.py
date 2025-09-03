def is_valid(isbn: str) -> bool:
    cleared_isbn = isbn.replace('-', '')
    if len(cleared_isbn) != 10:
        return False
    if not cleared_isbn[:-1].isdigit() or cleared_isbn[-1] not in '0123456789X':
        return False
    
    elements_sum = 0
    for index, letter in enumerate(cleared_isbn):
        if index == 9 and letter == 'X':
            elements_sum += 10
        else:
            elements_sum += int(letter) * (10 - index)

    return elements_sum % 11 == 0
        