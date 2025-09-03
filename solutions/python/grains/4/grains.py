def square(number):
    board = []
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    while len(board) < number:
        if len(board) == 0:
            board.append(1)
        else:
            board.append(1 << len(board))
            
    return board[-1]


def total():
    return (1 << 64) - 1
