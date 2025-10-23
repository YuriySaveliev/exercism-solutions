def score(x, y):
    radius_squared = x ** 2 + y ** 2
    if radius_squared <= 1 :
        return 10
    if radius_squared <= 25:
        return 5
    if radius_squared <= 100:
        return 1
    return 0
