"""
Module implements rotational cipher
"""
import string


def rotate(text: str, key: int) -> str:
    """
    Function applies rotational cipher
    """
    output = []
    letters = string.ascii_lowercase
    cipher = letters[key:] + letters[:key]
    table = str.maketrans(letters, cipher)
    
    for item in text:
        letter = ''
        if item.isalpha() and item.islower():
            letter = item.translate(table)
        elif item.isalpha():
            letter = item.lower().translate(table).upper()
        else:
            letter = item
        output.append(letter)
    return ''.join(output)
