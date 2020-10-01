# write your code here
import random


class Player:

    def __init__(self, name):
        self.name = name

    def make_move(self, matrix, symbol):
        move = self.ask_for_move()
        matrix[move[0]][move[1]] = symbol
        return matrix

    def ask_for_move(self):
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


class EasyAI(Player):

    def make_move(self, matrix, symbol):
        print('Making move level "easy"')
        return self.make_random_move(matrix, symbol)

    @staticmethod
    def make_random_move(matrix, symbol):
        possible_moves = find_empty_spots(matrix)
        selected_move = random.choice(possible_moves)
        matrix[selected_move[0]][selected_move[1]] = symbol
        return matrix

        # try_count = 0
        # while try_count < 100:
        #     x = random.randint(1, 3)
        #     y = random.randint(1, 3)
        #     if matrix[x][y] == " ":
        #         matrix[x][y] = symbol
        #         return matrix
        #     try_count += 1
        # print("Something went wrong. Could not find move")


class MediumAI(EasyAI):

    def make_move(self, matrix, symbol):
        print('Making move level "medium"')
        # Rule 1: Search for winning move
        move = self.find_winning_move(matrix, symbol)
        if move is not None:
            matrix[move[0]][move[1]] = symbol
            return matrix

        # Rule 2: Search for blocking move
        opponent_symbol = "O" if symbol == "X" else "X"
        move = self.find_winning_move(matrix, opponent_symbol)
        if move is not None:
            matrix[move[0]][move[1]] = symbol
            return matrix

        # Default: Make random move
        return self.make_random_move(matrix, symbol)

    @staticmethod
    def find_winning_move(matrix, symbol):
        for [x, y] in find_empty_spots(matrix):
            matrix[x][y] = symbol
            possible_outcome = determine_game_state(matrix)
            matrix[x][y] = " "
            if possible_outcome.count("wins") > 0:
                return [x, y]
        return None
        # for x in [1, 2, 3]:
        #     for y in [1, 2, 3]:
        #         if matrix[x][y] == " ":
        #             matrix[x][y] = symbol
        #             possible_outcome = determine_game_state(matrix)
        #             matrix[x][y] = " "
        #             if possible_outcome.count("wins") > 0:
        #                 return [x, y]
        # return None


class HardAI (MediumAI):
    def make_move(self, matrix, symbol):
        print('Making move level "hard"')
        # Rule 1: Search for winning move
        move = self.find_winning_move(matrix, symbol)
        if move is not None:
            matrix[move[0]][move[1]] = symbol
            return matrix

        # Rule 2: Search for blocking move
        opponent_symbol = "O" if symbol == "X" else "X"
        move = self.find_winning_move(matrix, opponent_symbol)
        if move is not None:
            matrix[move[0]][move[1]] = symbol
            return matrix

        # Rule 3: Brute force find best move (minimax)
        x, y = self.minimax_best_move(matrix, symbol)
        matrix[x][y] = symbol
        return matrix

    def minimax_best_move(self, matrix, symbol):
        best_score = 0
        best_move = []
        for [x, y] in find_empty_spots(matrix):
            current_score = self.calculate_score(x, y, matrix, symbol)
            if best_move == [] or current_score > best_score:
                best_score = current_score
                best_move = [x, y]
        return best_move[0], best_move[1]

    def calculate_score(self, move_x, move_y, matrix, symbol):
        game_state = determine_game_state(matrix)
        opponent_symbol = "O" if symbol == "X" else "X"
        if game_state[0] == symbol:
            return 10
        elif game_state[0] == opponent_symbol:
            return -10
        elif game_state == "Draw":
            return 0
        else:
            score = 0
            for [x, y] in find_empty_spots(matrix):
                matrix[x][y] = symbol
                score += self.calculate_score(x, y, matrix, symbol)
                matrix[x][y] = " "
            return score

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


def find_empty_spots(matrix):
    empty_spots = []
    for i in range(1, 4):
        for j in range(1, 4):
            if matrix[i][j] == " ":
                empty_spots.append([i, j])
    return empty_spots


def determine_game_state(matrix):
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
    elif len(find_empty_spots(matrix)) == 0:
        return "Draw"
    else:
        return "Game not finished"

# def ai_easy_move(matrix, symbol):
#     print('Making move level "easy"')
#     try_count = 0
#     while try_count < 100:
#         x = random.randint(1, 3)
#         y = random.randint(1, 3)
#         if matrix[x][y] == " ":
#             matrix[x][y] = symbol
#             return matrix
#         try_count += 1
#     print("Something went wrong. Could not find move")


def start_menu():
    player_types = ["user", "easy", "medium", "hard"]
    while True:
        command = input("Input command: ")
        if command == "exit":
            return None, None
        command_parts = command.split()
        if len(command_parts) < 3 or command_parts[0] != "start":
            print("Bad parameters!")
        elif command_parts[1] not in player_types or command_parts[2] not in player_types:
            print("Bad parameters!")
        else:
            return get_player(command_parts[1]), get_player(command_parts[2])


def get_player(player_type):
    if player_type == "user":
        return Player("Barny")
    elif player_type == "easy":
        return EasyAI("Dummy")
    elif player_type == "medium":
        return MediumAI("Not_So_Dumb")
    elif player_type == "hard":
        return HardAI("Genius")
    return None


# ------------ Start of game --------------------
# cell_string = input("Enter cells: ")
# game_matrix, number_of_xs, number_of_os = read_matrix(cell_string)
# main game loop
while True:
    player1, player2 = start_menu()
    # If user wants to exit, player1 will be exit
    if player1 is None:
        break

    # Set empty board
    number_of_symbols = {
        "X": 0,
        "O": 0
    }
    game_matrix, number_of_symbols["X"], number_of_symbols["O"] = read_matrix("         ")
    print_matrix(game_matrix)
    game_state = determine_game_state(game_matrix)
    first_players_turn = True
    while game_state == "Game not finished":
        # Determine next Symbol
        next_symbol = "O" if number_of_symbols["X"] > number_of_symbols["O"] else "X"
        # Determine next player
        next_player = player1 if first_players_turn else player2
        # Make move

        # Player move
        game_matrix = next_player.make_move(game_matrix, next_symbol)
        number_of_symbols[next_symbol] += 1

        print_matrix(game_matrix)
        game_state = determine_game_state(game_matrix)
        # If someone won with this move or it is a draw, end game
        if game_state != "Game not finished":
            break

        # Change players turn
        first_players_turn = not first_players_turn

    print(game_state)









