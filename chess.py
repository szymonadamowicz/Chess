import random

def generate_board():
    main_list = []
    for i in range(8):
        middle_list = []
        for j in range(8):
            middle_list.append(0)
        main_list.append(middle_list)
    return main_list


def placed_pawn(board):
    x = random.randrange(0, 8)
    y = random.randrange(0, 8)
    if board[x][y] == 0:
        board[x][y] = "P"
        return board
    else:
        return placed_pawn(board)


def placed_queens(num, board):
    for i in range(num):
        x = random.randrange(0, 8)
        y = random.randrange(0, 8)
        if board[x][y] == 0:
            board[x][y] = "Q"
            num -= 1
        else:
            return placed_queens(num, board)
    return board



