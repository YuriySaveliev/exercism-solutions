def saddle_points(matrix):
    if not all(len(item) == len(matrix[0]) for item in matrix):
        raise ValueError('irregular matrix')
    result = []
    for index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if max(row) == col:
                print(max(row))
                print(min([item[col_index] for item in matrix]))
                if min([item[col_index] for item in matrix]) == col:
                    result.append({'column': col_index + 1, 'row': index + 1})

    return result
