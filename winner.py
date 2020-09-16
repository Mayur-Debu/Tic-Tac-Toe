'''
check winners:
    check rows
    check columns
    check diagonals
'''

import os

board=[]

def display_new_list(board):
    print(board[0] + ' | ' +board[1] + ' | ' + board[2])
    print(board[3] + ' | ' +board[4] + ' | ' + board[5])
    print(board[6] + ' | ' +board[7] + ' | ' + board[8])


def check_playerX_winner(new_list):
    #check rows

    if (new_list[0]=='X' and new_list[1]=='X' and new_list[2]=='X' or
        new_list[3]=='X' and new_list[4]=='X' and new_list[5]=='X' or
        new_list[6]=='X' and new_list[7]=='X' and new_list[8]=='X'
        ):
            os.system('cls')
            print("*************************************************")
            print('player X won \n')
            board = new_list
            display_new_list(board)
            print("*************************************************")
            exit()

    #check columns
    elif (new_list[0]=='X' and new_list[3]=='X' and new_list[6]=='X' or
          new_list[1]=='X' and new_list[4]=='X' and new_list[7]=='X' or
          new_list[2]=='X' and new_list[5]=='X' and new_list[8]=='X'
         ):
            os.system('cls')
            print("*************************************************")
            print('player X won \n')
            board = new_list
            display_new_list(board)
            print("*************************************************")
            exit()


    #check diagonals
    elif (new_list[0]=='X' and new_list[4]=='X' and new_list[8]=='X' or
          new_list[6]=='X' and new_list[4]=='X' and new_list[2]=='X'
         ):
            print("*************************************************")
            print('player X won \n')
            board = new_list
            display_new_list(board)
            print("*************************************************")
            exit()

    else:
        pass


def check_playerO_winner(new_list):
    #check rows
    if (new_list[0]=='O' and new_list[1]=='O' and new_list[2]=='O' or
        new_list[3]=='O' and new_list[4]=='O' and new_list[5]=='O' or
        new_list[6]=='O' and new_list[7]=='O' and new_list[8]=='O'
        ):
            print("*************************************************")
            print('player O won \n')
            board = new_list
            display_new_list(board)
            print("*************************************************")
            exit()

    #check columns
    elif (new_list[0]=='O' and new_list[3]=='O' and new_list[6]=='O' or
          new_list[1]=='O' and new_list[4]=='O' and new_list[7]=='O' or
          new_list[2]=='O' and new_list[5]=='O' and new_list[8]=='O'
         ):
            print("*************************************************")
            print('player O won \n')
            board = new_list
            display_new_list(board)
            print("*************************************************")
            exit()

    #check diagonals
    elif (new_list[0]=='O' and new_list[4]=='O' and new_list[8]=='O' or
          new_list[6]=='O' and new_list[4]=='O' and new_list[2]=='O'
         ):
            print("*************************************************")
            print('player O won \n')
            board = new_list
            display_new_list(board)
            print("*************************************************")
            exit()
    else:
        pass
