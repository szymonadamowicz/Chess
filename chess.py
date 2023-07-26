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
    if not queens_captures:
        print("No")
    else:
        print("Yes")

    choices = [0, 1, 2, 3, 4]
    user_choice = 0
    while user_choice in choices:
        user_choice = int(input('''Next steps:
                1. Draw a new pawn position
                2. Removal of the given hetman
                3. Re-verification of the beating
                4. Showing the current layout of the playing field
                5. Exit
                '''))
        if user_choice == 1:
            final_board[pawn[0]][pawn[1]] = 0
            final_board, pawn = placed_pawn(final_board)
            print(f"New pawn's position: x = {pawn[0] + 1}, y = {pawn[1] + 1}")
        elif user_choice == 2:
            x = int(input("Give x of the queen you want to remove: ")) - 1
            y = int(input("Give y of the queen you want to remove: ")) - 1
            queens_length = len(queens)
            for queen in queens:
                if queen == [x, y]:
                    final_board[queen[0]][queen[1]] = 0
                    queens.remove(queen)
                    print("Queen has been removed")
            if queens_length == len(queens):
                print("There is no such a Queen")

        if user_choice == 3:
            queens_captures = verification(pawn, queens, final_board)
            print(f"Number of Queens: {number_of_queens}")
            print(f"Pawn's position: x = {pawn[0] + 1}, y = {pawn[1] + 1}")
            for queen in queens:
                print(f"Queen's position: x = {queen[0] + 1}, y = {queen[1] + 1}")
            print("Will the pawn be captured by the queen?")
            if not queens_captures:
                print("No")
            else:
                print("Yes")

        if user_choice == 4:
            for i in final_board:
                for j in i:
                    print(j, end=" ")
                print()