def is_isogram(string: str) -> bool:
    letters = set()
    string_norm = string.lower()
    for letter in string_norm:
        if not letter.isalpha():
            continue
        if letter in letters:
            return False
        letters.add(letter)
    return True
