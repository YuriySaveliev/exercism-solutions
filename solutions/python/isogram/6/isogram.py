def is_isogram(string):
    letters = []
    string_norm = string.lower()
    for letter in string_norm:
        if letter.isalpha() and letters.count(letter) > 0:
            return False
        letters.append(letter)
    return True
