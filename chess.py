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
        return board, [x, y]
    else:
        return placed_pawn(board)


def placed_queens(num, board):
    positions = []
    for i in range(num):
        x = random.randrange(0, 8)
        y = random.randrange(0, 8)
        if board[x][y] == 0:
            board[x][y] = "Q"
            num -= 1
            positions.append([x, y])
        else:
            return placed_queens(num, board)
    return board, positions


def check_diag(pawn, queen, board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == pawn:
                I, J = i, j
            if board[i][j] == queen:
                P, Q = i, j
    if P - Q == I - J or P + Q == I + J:
        return True
    else:
        return False


def verification(pawn, queens, board):
    captures = []
    for queen in queens:
        if pawn[0] == queen[0] or pawn[1] == queen[1] or check_diag("P", "Q", board):
            captures.append(queen)
    return captures


def menu():
    pass


if __name__ == '__main__':
    number_of_queens = random.randrange(6)
    gen_board = generate_board()
    pawn_board, pawn = placed_pawn(gen_board)
    final_board, queens = placed_queens(number_of_queens, pawn_board)
    queens_captures = verification(pawn, queens, final_board)

    print(f"Number of Queens: {number_of_queens}")
    print(f"Pawn's position: x = {pawn[0] + 1}, y = {pawn[1] + 1}")
    for queen in queens:
        print(f"Queen's position: x = {queen[0] + 1}, y = {queen[1] + 1}")
    for i in final_board:
        for j in i:
            print(j, end=" ")
        print()
    print("Will the pawn be captured by the queen?")
    if queens_captures == []:
        print("No")
    else:
        print("Yes")
