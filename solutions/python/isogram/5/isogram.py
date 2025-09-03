def is_isogram(string):
    letters = ''
    for letter in string.lower():
        if letter != '-' and letter != ' ' and letter in letters.lower():
            return False
        letters += letter
    return True
