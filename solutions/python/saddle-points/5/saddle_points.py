def saddle_points(matrix):
    if not all(len(item) == len(matrix[0]) for item in matrix):
        raise ValueError('irregular matrix')
    result = []
    for index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            is_saddle_point = max(row) == col and min(item[col_index] for item in matrix) == col
            if is_saddle_point:
                result.append({'column': col_index + 1, 'row': index + 1})

    return result
