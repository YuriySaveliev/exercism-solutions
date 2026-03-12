MAPPINGS = [
    {
        "value": 3,
        "word": "Pling"
    },
    {
        "value": 5,
        "word": "Plang"
    },
    {
        "value": 7,
        "word": "Plong"
    },
]


def convert(number: int) -> str:
    if all(number % item["value"] != 0 for item in MAPPINGS):
        return str(number) 
    else:
        return ''.join([item["word"] for item in MAPPINGS if number % item["value"] == 0])