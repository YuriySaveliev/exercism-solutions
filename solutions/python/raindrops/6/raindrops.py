"""Function converts number to string sequence"""

MAPPINGS = [
    (3, "Pling"),
    (5, "Plang"),
    (7, "Plong"),
]

def convert(number: int) -> str:
    if all(number % item[0] != 0 for item in MAPPINGS):
        return str(number) 
    return "".join(item[1] for item in MAPPINGS if number % item[0] == 0)