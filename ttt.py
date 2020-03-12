import os
import random
import time

def init_board():
    board = [[" ", " ", " "] , [" ", " ", " "] , [" ", " ", " "]]
    return board

def get_move(board, player):
    row, col = 0, 0
    wisely = False
    while not wisely:
        in_cord = input("You must choose, choose wisely! :")
        if (in_cord[0].upper() in 'ABC') and (in_cord[1] in '123') and len(in_cord) == 2:
            if in_cord[0].upper() == "A":
                row = 0
            elif in_cord[0].upper() == "B":
                row = 1
            elif in_cord[0].upper() == "C":
                row = 2
            if in_cord[1] == "1":
                col = 0
            elif in_cord[1] == "2":
                col = 1
            elif in_cord[1] == "3":
                col = 2
            if board[row][col] == " ":
                wisely = True
            else:
                print("That place is occupied")
        elif in_cord.upper() == 'QUIT':
            return "QUIT" , "QUIT"
        else:
            print("Invalid input")
    return row, col

def get_ai_move(board, player):
    row , col = 0 , 0
    if player == 1:
        selected = 'O'
    elif player == 2:
        selected = 'X'
    if board[0][0] == selected and board[0][1] == selected:
        row, col = 0, 2
    if board[0][0] == selected:
        row, col = 2, 2
    #decisions
    if board[row][col] != ' ':
        got_random = False
        while not got_random:
            row = random.randrange(0,3)
            col = random.randrange(0,3)
            if board[row][col] is ' ':
                got_random = True
        return row, col
    elif board[row][col] is ' ':
        return row, col


def mark(board, player, row, col):
    if board[row][col] == " ":
        if player == 1:
            board[row][col] = 'X'
        elif player == 2:
            board[row][col] = 'O'
    else:
        pass

def has_won(board, player):
    if player == 1:
        selected = 'X'
    elif player == 2:
        selected = 'O'
    if board[0] == [selected, selected, selected]:
        return True
    elif board[1] == [selected, selected, selected]:
        return True
    elif board[2] == [selected, selected, selected]:
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
    if " " in board[0] or board[1] or board[2]:
        return False
    else:
        return True

def print_board(board):
    print("    1   2   3\n")
    print("A   "+str(board[0][0])+" | "+str(board[0][1])+" | "+str(board[0][2])+"")
    print("   ---+---+---")
    print("B   "+str(board[1][0])+" | "+str(board[1][1])+" | "+str(board[1][2])+"")
    print("   ---+---+---")
    print("C   "+str(board[2][0])+" | "+str(board[2][1])+" | "+str(board[2][2])+"")

def print_result(winner):
    if winner == 0:
        print("It's a tie!")
    else:
        print("Player " + str(winner)+ " has won!")

def tictactoe_game(mode):
    os.system("clear")  
    player = 1
    end = False
    winner = 0
    board = init_board()
    while not end:
        print_board(board)
        print("Current turn: X")
        if mode == 'HUMAN-HUMAN' or 'HUMAN-AI':
            row, col = get_move(board, player)
            if row == 'QUIT':
                print("\n\nGood bye!\n")
                time.sleep(1)
                quit()
        if mode == 'AI-AI':
            row, col = get_ai_move(board,player)
        mark(board, player, row, col)
        print_board(board)
        if has_won(board, player) == True:
            winner = player
            end = True
            continue
        if is_full(board):
            end = True
            winner = 0
        player += 1
        os.system("clear")
        print_board(board)
        print("Current turn: O")
        if mode  == 'HUMAN-HUMAN':
            row, col = get_move(board , player)
        elif mode == 'HUMAN-AI' or 'AI-AI':
            row, col = get_ai_move(board , player)
        mark(board,player,row,col)
        print_board(board)
        if has_won(board, player) == True:
            winner = player
            end = True
            continue
        if is_full(board):
            end = True
            winner = 0
        player -= 1
        os.system("clear")
    os.system("clear")
    print_board(board)
    print_result(winner)

def main_menu():
    tictactoe_game('HUMAN-AI')


if __name__ == '__main__':
    main_menu()