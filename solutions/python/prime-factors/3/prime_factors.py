def factors(value: int) -> list[int]:
    value_factors = []
    f = value
    
    item = 2
    while f > 1:
        while f % item == 0:
            value_factors.append(item)
            f //= item
        item += 1

    return value_factors
