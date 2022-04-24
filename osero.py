#!/bin/python3
import sys
import time
import random
import datetime
import numpy as np

import cpu

cell = 8
white = -1
blank = 0
black = 1

player_white = ["cpu", "deep1_forbid"]
player_black = ["cpu", "table"]

kihu_white = []
kihu_black = []

support = True

kihu = True

kihu_read = False
kihu_read_file = "kihu/kihu.txt"
kihu_read_cnt = 0

if kihu_read:
    player_white = ["", ""]
    player_black = ["", ""]
    kihu = False


start_turn = black

vec = [-1, 0, 1]

#board = [[0 for i in range(cell)]for j in range(cell)]
#board = np.array(board)
#board[3][4] = black
#board[4][3] = black
#board[3][3] = white
#board[4][4] = white

if kihu_read:
    with open(kihu_read_file, mode = "r") as f:
        kihulist = f.readlines()
    for i, line in enumerate(kihulist):
        tmp = list(map(int, line.split()))
        kihulist[i] = tmp
    kihu_len = len(kihulist)

if kihu:
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    filepath = "./kihu/kihu" + now.strftime('%Y%m%d-%H%M%S') + ".txt"
    #filepath = "./kihu/kihu.txt"
    f =  open(filepath, mode = "w")
    f.close()

def main(turn, board):
    put_able_cnt, board = put_able_check(turn, board)
    print_out(board)
    if put_able_cnt == 0:
        fin_flag, winner = fin_game_check(turn, board, True)
    else:
        if turn == white:
            print("turn : white")
            if player_white[0] == "cpu":
                x, y = computer(turn, board, player_white[1])
            else:
                x, y = input_num(board)
        else:
            print("turn : black")
            if player_black[0] == "cpu":
                x, y = computer(turn, board, player_black[1])
            else:
                x, y = input_num(board)

        if turn == white:
            kihu_white.append([x,y])
        else:
            kihu_black.append([x,y])
        if kihu:
            with open(filepath, mode = "a") as f:
                f.write("{} {}\n".format(x, y))
        board = convert(x, y, turn, board)

        fin_flag, winner = fin_game_check(turn, board)
        #time.sleep(1)
    if fin_flag:
        return winner
    winner = main(turn*-1, board)
    return winner

def computer(turn, board, mode = "random"):
    if mode == "random":
        x,y = cpu.cpu_random(board)
    elif mode == "deep1":
        x,y = cpu.cpu_weak(board, turn)
    elif mode == "deep1_forbid":
        x,y = cpu.cpu_weak_forbid(board, turn)
    elif mode == "deep":
        x,y = cpu.cpu_deep(board, turn, 3)
    elif mode == "table":
        x,y = cpu.cpu_table(board, turn)
    else:
        x,y = cpu.cpu_random(board)
    return x, y


def fin_game_check(turn, board, passpass = False):
    winner = 0
    white_num = np.count_nonzero(board == white)
    black_num = np.count_nonzero(board == black)
    fin_game = False
    if white_num == 0 or black_num == 0:
        print_out(board)
        fin_game = True
    if (not 0 in board):
        print_out(board)
        fin_game = True
    if passpass:
        put_able_cnt, tmp = put_able_check(turn * -1, board)
        if put_able_cnt == 0:
            fin_game = True
        else:
            print("pass")

    if fin_game:
        print("white : " + str(white_num) + "   black : " + str(black_num))
        if white_num == black_num:
            winner = 0
            print("draw")
        elif white_num > black_num:
            winner = white
            print("win white")
        elif white_num < black_num:
            winner = black
            print("win black")
    return fin_game, winner


def convert(x, y, turn, board):
    for i in vec:
        for j in vec:
            check_bool, endx, endy = put_check(x, y, i, j, turn, board)
            if check_bool:
                tmpx = x
                tmpy = y
                while True:
                    board[tmpx][tmpy] = turn
                    tmpx += i
                    tmpy += j
                    if tmpx == endx and tmpy == endy:
                        break

    for i in range(cell):
        for j in range(cell):
            if board[i][j] == 2:
                board[i][j] = 0
    return board


def put_able_check(turn, board):
    put_able_cnt = 0
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == white or board[i][j] == black:
                continue
            
            for k in vec:
                for l in vec:
                    put_bool, tmp, tmp = put_check(i, j, k, l, turn, board)
                    if put_bool:
                        #print(i, j, k, l, put_bool)
                        board[i][j] = 2
                        put_able_cnt += 1
                        break
                else:
                    continue
                break
    return put_able_cnt, board


def put_check(x, y, vecx, vecy, turn, board):
    x += vecx
    y += vecy
    if x < 0 or y < 0 or x > cell-1 or y > cell-1:
        return False, x, y
    if board[x][y] == turn:
        return False, x, y
    if board[x][y] == blank or board[x][y] == 2:
        return False, x, y

    while True:
        x += vecx
        y += vecy
        if x < 0 or y < 0 or x > cell-1  or y > cell-1:
            return False, x, y
        if board[x][y] == blank or board[x][y] == 2:
            return False, x, y
        if board[x][y] == turn:
            return True, x, y
    return False, x, y


def input_num(board):
    global kihu_read
    global kihu_read_cnt
    while True:
        try:
            if kihu_read:
                x = kihulist[kihu_read_cnt][0]
                y = kihulist[kihu_read_cnt][1]
                kihu_read_cnt += 1
                if kihu_read_cnt >= kihu_len:
                    kihu_read = False
            else:
                x, y = map(int, input().split())
            if  x < 0 or 7 < x or y < 0 or 7 < y:
                print("x and y is 0~7")
            else :
                if board[x][y] == 2:
                    break
                elif board[x][y] == 1 or board[x][y] == -1:
                    print("already storne")
                else :
                    print("not put")
        except (TypeError, ValueError):
            print("again")
            pass
    return x, y


def print_out(board):
    print(" |", end="")
    for i in range(cell):
        print(" {0} ".format(i), end="|")
    print()
    print("ーーーーーーーーーーーーーーーーー")
    for i in range(cell):
        print(i, end = "|")
        for j in range(cell):
            if board[i][j] == black:
                print(" ○ ", end="|")
            elif board[i][j] == white:
                print(" ● ", end="|")
            elif board[i][j] == 2 and support:
                print(" ･ ", end="|")
            else :
                print("   ", end="|")
        print("")
        print("ーーーーーーーーーーーーーーーーー")

def board_new():
    board = [[0 for i in range(cell)]for j in range(cell)]
    board = np.array(board)
    board[3][4] = black
    board[4][3] = black
    board[3][3] = white
    board[4][4] = white
    return board

if __name__ == '__main__':
    board = board_new()
    winner = main(start_turn, board)

    cpu.q_learning.new_table()

    #win_white = 0
    #win_black = 0
    #drawww    = 0
    #n = 100
    #for i in range(n):
    #    kihu_white = []
    #    kihu_black = []
    #    
    #    board = board_new()
    #    winner = main(start_turn, board)
    #    
    #    white_table = np.load("white_table.npy")
    #    black_table = np.load("black_table.npy")
    #    if winner == white:
    #        win_white += 1
    #        for li in kihu_white:
    #            white_table[li[0]][li[1]] += 1
    #        for li in kihu_black:
    #            black_table[li[0]][li[1]] -= 1
    #    elif winner == black:
    #        win_black += 1
    #        for li in kihu_white:
    #            white_table[li[0]][li[1]] -= 1
    #        for li in kihu_black:
    #            black_table[li[0]][li[1]] += 1
    #    else:
    #        drawww += 1
    #        for li in kihu_white:
    #            white_table[li[0]][li[1]] -= 1
    #        for li in kihu_black:
    #            black_table[li[0]][li[1]] += 1
    #    #print(white_table)
    #    #print("=======================")
    #    #print(black_table)
    #    ##time.sleep(1)
    #    #np.save("white_table.npy", white_table)
    #    #np.save("black_table.npy", black_table)

    #        

    #    print("white : ", win_white, "  ", win_white / (i+1) * 100, "%")
    #    print("black : ", win_black, "  ", win_black / (i+1) * 100, "%")
    #    print("draw  : ", drawww, "  ", drawww / (i+1) * 100, "%")
