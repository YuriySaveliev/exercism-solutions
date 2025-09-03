def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a != strand_b for strand_a, strand_b in zip(strand_a, strand_b))
