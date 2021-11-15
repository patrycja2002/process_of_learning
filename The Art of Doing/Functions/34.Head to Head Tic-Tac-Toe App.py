# Functions Challenge 34: Head to Head Tic-Tac-Toe App

def draw_board(list_):
    print("\n\t Tic - Tac - Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + list_[0] + " || " + list_[1] + " || " + list_[2] + " ||")
    print("\t|| " + list_[3] + " || " + list_[4] + " || " + list_[5] + " ||")
    print("\t|| " + list_[6] + " || " + list_[7] + " || " + list_[8] + " ||")
    print("\t~~~~~~~~~~~~~~~~~")


def get_player_input(player_character, list_):
    while True:
        player_move = int(input(player_character + ": Where would you like to place your piece(1 - 9): "))
        if 0 < player_move < 10:
            if list_[player_move - 1] == "_":
                return player_move
            else:
                print("That spot has already been chosen.  Try again.")
        else:
            print("That is not a spot on the board.  Try again.")


def place_char_on_board(player_character, player_move, list_):
    list_[player_move - 1] = player_character


def is_winner(player_character, list_):
    return ((list_[0] == player_character and list_[1] == player_character and list_[2] == player_character) or
            (list_[3] == player_character and list_[4] == player_character and list_[5] == player_character) or
            (list_[6] == player_character and list_[7] == player_character and list_[8] == player_character) or
            (list_[0] == player_character and list_[3] == player_character and list_[6] == player_character) or
            (list_[1] == player_character and list_[4] == player_character and list_[7] == player_character) or
            (list_[2] == player_character and list_[5] == player_character and list_[8] == player_character) or
            (list_[0] == player_character and list_[4] == player_character and list_[8] == player_character) or
            (list_[2] == player_character and list_[4] == player_character and list_[6] == player_character))


player_1 = "X"
player_2 = "O"
c_list = ['_']*9
n_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

draw_board(n_list)
draw_board(c_list)

while True:
    move = get_player_input(player_1, c_list)
    place_char_on_board(player_1, move, c_list)
    draw_board(n_list)
    draw_board(c_list)
    if is_winner(player_1, c_list):
        print("Player 1 wins!")
        break
    elif "_" not in c_list:
        print("The game was a tie!")
        break

    move = get_player_input(player_2, c_list)
    place_char_on_board(player_2, move, c_list)
    draw_board(n_list)
    draw_board(c_list)
    if is_winner(player_2, c_list):
        print("Player 2 wins!")
        break
