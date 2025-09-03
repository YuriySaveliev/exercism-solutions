def factors(value: int) -> list[int]:
    value_factors = []
    f = value
    
    for item in range(2, value + 1):
        while f % item == 0:
            value_factors.append(item)
            f = f / item
        if f == 1:
            break

    return value_factors
