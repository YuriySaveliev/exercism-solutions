"""Function converts number to string sequence"""

MAPPINGS = [
    (3, "Pling"),
    (5, "Plang"),
    (7, "Plong"),
]

def convert(number: int) -> str:
    if all(number % factor for factor, sound in MAPPINGS):
        return str(number) 
    return "".join(sound for factor, sound in MAPPINGS if not number % factor)