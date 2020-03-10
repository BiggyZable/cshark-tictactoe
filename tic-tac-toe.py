def init_board():
    board = [[0, 0, 0] , [0, 0, 0] , [0, 0, 0]]
return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
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
    """Prints a 3-by-3 board on the screen with borders."""
    pass


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
