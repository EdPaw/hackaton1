import random

matrix = [["1️⃣", "2️⃣", "3️⃣"],
          ["4️⃣", "5️⃣", "6️⃣"],
          ["7️⃣", "8️⃣", "9️⃣"]]

# selection, row, column
SELECTION_DICT = [
    {"selection": 1, "row": 0, "column": 0},
    {"selection": 2, "row": 0, "column": 1},
    {"selection": 3, "row": 0, "column": 2},
    {"selection": 4, "row": 1, "column": 0},
    {"selection": 5, "row": 1, "column": 1},
    {"selection": 6, "row": 1, "column": 2},
    {"selection": 7, "row": 2, "column": 0},
    {"selection": 8, "row": 2, "column": 1},
    {"selection": 9, "row": 2, "column": 2},
]

#SIGNS = ["🟢", "❌"]


def print_matrix(any_matrix):
    for row in any_matrix:
        for element in row:
            print(element, end=" ")
        print()


def player_turn(player_sign, game_matrix, taken):

    while True:
        player = input(f"\nPlayer {player_sign}, mark position 1-9: ")
        if player.isdigit():
            player = int(player)
            if player in range(1, 10):
                break

    dicty = SELECTION_DICT[player - 1]
    row = dicty["row"]
    column = dicty["column"]

    if game_matrix[row][column] == "🟢" or game_matrix[row][column] == "❌":
        print("Place already taken. You lost your turn\n")
        print_matrix(game_matrix)
        return game_matrix
    else:
        game_matrix[row][column] = player_sign
        print_matrix(game_matrix)
        taken.append(player-1)
        return game_matrix, taken


def computer_turn(player_sign, game_matrix, taken):

    while True:
        computer = random.randint(1, 9)
        if computer-1 not in taken:
            break

    print(f"\nComputer {player_sign}, mark position: {computer}")
    dicty = SELECTION_DICT[computer - 1]
    row = dicty["row"]
    column = dicty["column"]

    game_matrix[row][column] = player_sign
    print_matrix(game_matrix)
    taken.append(computer - 1)
    return game_matrix, taken


def win_horizontal(game_matrix):
    for row in game_matrix:
        if row[0] == row[1] == row[2]:
            return True


def win_vertical(game_matrix):
    for col in range(3):
        if game_matrix[0][col] == game_matrix[1][col] == game_matrix[2][col]:
            return True


def win_diagonally(game_matrix):
    if game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2]:
        return True
    if game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0]:
        return True


def win_all(game_matrix):
    if win_horizontal(game_matrix) or win_vertical(game_matrix) or win_diagonally(game_matrix):
        return True


def check_win(player_sign, turn, game_matrix):
    turn += 1
    if win_all(game_matrix):
        print(f"\nThe winner is {player_sign}. Congratulations!")
        return True
    if turn == 10:
        print("There is no winner")
        return True


def type_of_game():
    print("TIC TAC TOE GAME")
    while True:
        vs = input("Do you want to play with PC or another Player? Enter PC or P: ").upper()
        if vs == "PC" or vs == "P":
            break

    if vs == "P":
        vs_pretty = "player"
    elif vs == "PC":
        vs_pretty = "computer"

    return vs_pretty


def main():

    vs_pretty = type_of_game()
    taken = []
    print_matrix(matrix)

    turn = 1
    win1 = False
    win2 = False

    while True:
        player_turn("🟢", matrix, taken)
        win1 = check_win("🟢", turn, matrix)
        if turn == 10 or win1 or win2:
            break

        if vs_pretty == "computer":
            computer_turn("❌", matrix, taken)
        elif vs_pretty == "player":
            player_turn("❌", matrix, taken)

        win2 = check_win("❌", turn, matrix)
        if turn == 10 or win1 or win2:
            break


main()

