def is_isogram(string):
    norm_string = string.lower()
    for letter in norm_string:
        if letter == ' ' or letter == '-':
            continue
        elif norm_string.count(letter) > 1:
            return False        
    return True