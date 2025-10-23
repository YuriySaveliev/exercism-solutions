def score(x, y):
    radius_squared = x ** 2 + y ** 2
    if radius_squared <= 1 :
        result_score = 10
    elif radius_squared <= 25:
        result_score = 5
    elif radius_squared <= 100:
        result_score = 1
    elif radius_squared > 100:
        result_score = 0

    return result_score
