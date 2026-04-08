"""
Module implements rotational cipher
"""
import string


def rotate(text: str, key: int) -> str:
    """
    Function applies rotational cipher
    """
    letters = string.ascii_lowercase
    cipher = letters[key:] + letters[:key]
    table = str.maketrans(letters + letters.upper(), cipher + cipher.upper())
    
    return text.translate(table)
