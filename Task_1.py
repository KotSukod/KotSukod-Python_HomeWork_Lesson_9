# Создайте программу для игры в ""Крестики-нолики"".

import random

def print_board(board):
    print(board[0], end = ' ')
    print(board[1], end = ' ')
    print(board[2])
    print(board[3], end = ' ')
    print(board[4], end = ' ')
    print(board[5])
    print(board[6], end = ' ')
    print(board[7], end = ' ')
    print(board[8])

def chance_turn(x):
    if x == 2:
        print ("Ходит игорок {}".format(player_1))
        token = "X"
        return  1
    else:    
        print ("Ходит игорок {}".format(player_2))
        token = "O"
        return 2 

def player_turn(board,token,step):
    while board[step -1] == 'X' or board[step -1] == 'O':
        print ("Эта клетка занята")
        step = int(input("Ваш ход: "))
    else:
        ind = board.index(step)    
        board[ind] = token

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def get_result():
    win = ""
 
    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"   
    return win

board = list(range(1,10))

player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")

fist_turn = random.randint(1, 2)
if fist_turn == 1:
    play_turn = 2
    token = 'X'
else:
    play_turn = 1
    token = 'O'

game_over = False

while game_over == False:
    play_turn = chance_turn(play_turn)
    if play_turn == 1:
        token = 'X'
    else:
        token = 'O'    
    step = int(input("Ваш ход: "))
    player_turn(board,token,step)
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
    print_board(board)
if play_turn == 1:
    print("Победил игрок {}".format(player_1))
else:
    print("Победил игрок {}".format(player_2))

