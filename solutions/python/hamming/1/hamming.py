def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    h_distance = 0
    for index, item in enumerate(strand_a):
        if strand_a[index] != strand_b[index]:
            h_distance += 1
    return h_distance
