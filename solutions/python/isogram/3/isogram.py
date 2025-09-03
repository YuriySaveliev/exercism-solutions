import re


def is_isogram(string):
    cleaned_string = re.sub(r'[^a-z]', '', string.lower())
    return len(cleaned_string) == len(set(cleaned_string))
