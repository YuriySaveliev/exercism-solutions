"""
Module implements rotational cipher
"""
import string


def rotate(text: str, key: int) -> str:
    """
    Function applies rotational cipher
    """
    letters = string.ascii_lowercase + string.ascii_uppercase
    lowercase_shifted = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    uppercase_shifted = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    cipher = lowercase_shifted + uppercase_shifted
    table = str.maketrans(letters, cipher)
    
    return text.translate(table)
