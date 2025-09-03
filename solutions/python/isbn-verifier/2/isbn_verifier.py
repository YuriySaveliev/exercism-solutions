def is_valid(isbn: str) -> bool:
    cleared_isbn = isbn.split('-')
    cleared_isbn = ''.join(cleared_isbn)
    if len(cleared_isbn) != 10 or not all(item.isdigit() for item in cleared_isbn[:-1]) or (not cleared_isbn.endswith('X') and cleared_isbn[-1].isalpha()):
        return False
    elements_sum = 0
    for index, letter in enumerate(cleared_isbn):
        if index == len(cleared_isbn) - 1 and letter == 'X':
            elements_sum += 10
        else:
            elements_sum += int(letter) * (10 - index)
            
    return elements_sum % 11 == 0
        