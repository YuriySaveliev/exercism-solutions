import string


def rotate(text: str, key: int) -> str:
    output = []
    letters = string.ascii_lowercase
    cipher = f'{letters[key:]}{letters[:key]}'
    for item in text:
        if item.isalpha():
            if item.lower() == item:
                output.append(cipher[letters.index(item)])
            else:
                output.append(cipher[letters.index(item.lower())].upper())
        else:
            output.append(item)
    return ''.join(output)