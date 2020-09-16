'''
Tasks that we need to perform :
1. Make a board
2. Play Game
    #Display Board
    #Choose Position
'''
import winner
import os

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
new_list = []


def display_board():
    print(board[0] + ' | ' +board[1] + ' | ' + board[2])
    print(board[3] + ' | ' +board[4] + ' | ' + board[5])
    print(board[6] + ' | ' +board[7] + ' | ' + board[8])


def playerX_turn():
    if '-' in board:
        print("\nPlayer X turn:")
        position = int(input("Enter the postion from 1-9"))
        if board[position] == 'O' or board[position] == 'X':
            os.system('cls')
            print("Sorry Slot Full!!!\n")
            display_board()
            playerX_turn()

        else:
            os.system('cls')
            board[position]='X'
            new_list=board
            winner.check_playerX_winner(new_list)
            display_board()
            playerO_turn()
    else:
        os.system('cls')
        print("*************************************************")
        print('Nobody Won It\'s a Tie.\n')
        print("*************************************************")
        exit()

def playerO_turn():
    if '-' in board:
        print("\nPlayer O turn:")
        position = int(input("Enter the postion from 1-9"))
        # position = int(position) - 1
        if board[position] == 'X' or board[position] == 'O':
            os.system('cls')
            print("Sorry Slot Full!!!\n")
            display_board()
            playerO_turn()

        else:
            os.system('cls')
            board[position] = "O"
            new_list = board
            winner.check_playerO_winner(new_list)
            display_board()
            playerX_turn()
    else:
        os.system('cls')
        print("*************************************************")
        print('Nobody Won It\'s a Tie.\n')
        print("*************************************************")
        exit()


if __name__ == '__main__':
     display_board()
     playerX_turn()

