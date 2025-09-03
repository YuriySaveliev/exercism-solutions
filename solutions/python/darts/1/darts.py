def score(x, y):
    radius = (x ** 2 + y ** 2) ** 0.5
    if radius <= 1 :
        result_score = 10
    elif radius <= 5:
        result_score = 5
    elif radius <= 10:
        result_score = 1
    elif radius > 10:
        result_score = 0

    return result_score
