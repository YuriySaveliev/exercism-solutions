def factors(value: int) -> list[int]:
    value_factors = []
    fraction = value
    
    factor = 2
    while fraction > 1:
        while fraction % factor == 0:
            value_factors.append(factor)
            fraction //= factor
        factor += 1

    return value_factors
