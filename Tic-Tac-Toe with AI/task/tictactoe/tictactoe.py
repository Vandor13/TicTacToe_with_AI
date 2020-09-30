# write your code here

def read_matrix(matrix_string):
    matrix_string = matrix_string.replace("_", " ")
    no_of_os = matrix_string.count("O")
    no_of_xs = matrix_string.count("X")
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    matrix[1][3] = matrix_string[0]
    matrix[2][3] = matrix_string[1]
    matrix[3][3] = matrix_string[2]
    matrix[1][2] = matrix_string[3]
    matrix[2][2] = matrix_string[4]
    matrix[3][2] = matrix_string[5]
    matrix[1][1] = matrix_string[6]
    matrix[2][1] = matrix_string[7]
    matrix[3][1] = matrix_string[8]
    return matrix, no_of_xs, no_of_os


def print_matrix(matrix):
    print("---------")
    print("| {} {} {} |".format(matrix[1][3], matrix[2][3], matrix[3][3]))
    print("| {} {} {} |".format(matrix[1][2], matrix[2][2], matrix[3][2]))
    print("| {} {} {} |".format(matrix[1][1], matrix[2][1], matrix[3][1]))
    print("---------")


def ask_for_move():
    while True:
        try:
            move = [int(c) for c in input("Enter the coordinates: ").split()]
            if not 1 <= move[0] <= 3 or not 1 <= move[1] <= 3:
                print("Coordinates should be from 1 to 3!")
            elif game_matrix[move[0]][move[1]] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                return move
        except:
            print("You should enter numbers!")


def determine_game_state(matrix, no_of_symbols):
    winner = ""
    # check horizontal win condition
    if matrix[1][3] == matrix[2][3] == matrix[3][3] and matrix[1][3] != " ":
        winner = matrix[1][3]
    elif matrix[1][2] == matrix[2][2] == matrix[3][2] and matrix[1][2] != " ":
        winner = matrix[1][2]
    elif matrix[1][1] == matrix[2][1] == matrix[3][1] and matrix[1][1] != " ":
        winner = matrix[1][1]
    # check vertical win condition
    elif matrix[1][3] == matrix[1][2] == matrix[1][1] and matrix[1][3] != " ":
        winner = matrix[1][3]
    elif matrix[2][3] == matrix[2][2] == matrix[2][1] and matrix[2][3] != " ":
        winner = matrix[2][3]
    elif matrix[3][3] == matrix[3][2] == matrix[3][1] and matrix[3][3] != " ":
        winner = matrix[3][3]
    # check diagonal win condition
    elif matrix[1][3] == matrix[2][2] == matrix[3][1] and matrix[1][3] != " ":
        winner = matrix[1][3]
    elif matrix[1][1] == matrix[2][2] == matrix[3][3] and matrix[1][1] != " ":
        winner = matrix[1][1]

    if winner != "":
        return "{} wins".format(winner)
    elif no_of_symbols >= 9:
        return "Draw"
    else:
        return "Game not finished"


cell_string = input("Enter cells: ")
game_matrix, number_of_xs, number_of_os = read_matrix(cell_string)

print_matrix(game_matrix)

next_move = ask_for_move()
if number_of_xs > number_of_os:
    game_matrix[next_move[0]][next_move[1]] = "O"
    number_of_os += 1
else:
    game_matrix[next_move[0]][next_move[1]] = "X"
    number_of_xs += 1

print_matrix(game_matrix)
print(determine_game_state(game_matrix, number_of_xs + number_of_os))









