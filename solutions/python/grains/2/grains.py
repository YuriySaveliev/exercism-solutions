def square(number):
    board = []
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    while len(board) < number:
        if len(board) == 0:
            board.append(1)
        else:
            board.append(board[len(board) - 1] * 2)
            
    return board[-1]


def total():
    board = []
    total_grain = 0

    while len(board) < 64:
        if len(board) == 0:
            grains = 1
        else:
            grains = board[len(board) - 1] * 2
        board.append(grains)
        total_grain += grains
    return sum(board)