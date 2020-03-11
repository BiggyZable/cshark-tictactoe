def init_board():
    board = [[0, 0, 0] , [0, 0, 0] , [0, 0, 0]]
    return board

def get_move(board, player):
    row, col = 0, 0
    wisely = False
    while not wisely:
        in_cord = input("You must choose, choose wisely! :")
        if (in_cord[0].upper() in 'ABC') and (in_cord[1] in '123') and len(in_cord) == 2:
            if in_cord[0] == "A":
                row = 0
            elif in_cord[0] == "B":
                row = 1
            elif in_cord[0] == "C":
                row = 2
            if in_cord[1] == "1":
                col = 0
            elif in_cord[1] == "2":
                col = 1
            elif in_cord[1] == "3":
                col = 2
            if board[row][col] == 0:
                print("in board")
                wisely = True
            else:
                print("place is occupied")
        else:
            print("Invalid input")
    return row, col

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col

def mark(board, player, row, col):
    if board[row][col] == 0:
        if player == 'X':
            board[row][col] = 'X'
        elif player == 'O':
            board[row][col] = 'O'
    else:
        pass

def has_won(board, player):
    selected = player
    if board[0] == [selected, selected, selected]:
        return True
    elif board[1] == [selected, selected, selected]:
        return True
    elif board[0] == [selected, selected, selected]:
        return True
    elif board[0][0] == selected and board[1][0] == selected and board[2][0] == selected:
        return True
    elif board[0][1] == selected and board[1][1] == selected and board[2][1] == selected:
        return True 
    elif board[0][2] == selected and board[1][2] == selected and board[2][2] == selected:
        return True 
    elif board[0][0] == selected and board[1][1] == selected and board[2][2] == selected:
        return True
    elif board[0][2] == selected and board[1][1] == selected and board[2][0] == selected:
        return True
    else:
        return False

def is_full(board):
    if 0 not in board:
        return True
    else:
        return False


def print_board(board):
    print(    1   2   3 

A   board[0][0] | board[0][1] | board[0][2] 
   ---+---+---
B   board[1][0] | board[1][1] | board[1][2] 
   ---+---+---
C   board[2][0] | board[2][1] | board[2][2] )
    


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
