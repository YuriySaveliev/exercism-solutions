scores = {
            'AEIOULNRST': 1,
            'DG': 2,
            'BCMP': 3,
            'FHVWY': 4,
            'K': 5,
            'JX': 8,
            'QZ': 10,
        }
def score(word):
    total_score = 0
    word = word.upper()
    for letter in word:
        for item in scores.keys():
            if letter in item:
                total_score += scores[item]
    return total_score
