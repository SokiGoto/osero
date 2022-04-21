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

player_white = ["cpu", "random"]
player_black = ["cpu", "deep1"]

support = True

kihu = True

kihu_read = False
kihu_read_file = "kihu/kihu20220419-140000.txt"
kihu_read_cnt = 0

start_turn = black

vec = [-1, 0, 1]

board = [[0 for i in range(cell)]for j in range(cell)]
board = np.array(board)
board[3][4] = black
board[4][3] = black
board[3][3] = white
board[4][4] = white

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
    f =  open(filepath, mode = "w")
    f.close()

def main(turn):
    put_able_cnt = put_able_check(turn)
    print_out()
    if put_able_cnt == 0:
        fin_game_check(turn, True)
        print("pass")
        main(turn*-1)

    if turn == white:
        print("turn : white")
        if player_white[0] == "cpu":
            x, y = computer(turn, player_white[1])
        else:
            x, y = input_num()
    else:
        print("turn : black")
        if player_black[0] == "cpu":
            x, y = computer(turn, player_black[1])
        else:
            x, y = input_num()

    if kihu:
        with open(filepath, mode = "a") as f:
            f.write("{} {}\n".format(x, y))
    convert(x, y, turn)

    fin_game_check(turn)
    #time.sleep(1)
    main(turn*-1)

def computer(turn, mode = "random"):
    if mode == "random":
        x,y = cpu.cpu_random(board)
    elif mode == "deep1":
        x,y = cpu.cpu_weak(board, turn)
    else:
        x,y = cpu.cpu_random(board)
    return x, y


def fin_game_check(turn, passpass = False):
    white_num = np.count_nonzero(board == white)
    black_num = np.count_nonzero(board == black)
    fin_game = False
    if white_num == 0 or black_num == 0:
        fin_game = True
    if (not 0 in board):
        fin_game = True
    if passpass:
        put_able_cnt = put_able_check(turn * -1)
        if put_able_cnt == 0:
            fin_game = True

    if fin_game:
        print_out()
        print("white : " + str(white_num) + "   black : " + str(black_num))
        if white_num == black_num:
            print("draw")
            time.sleep(1)
            exit()
        elif white_num > black_num:
            print("win white")
            time.sleep(1)
            exit()
        elif white_num < black_num:
            print("win black")
            time.sleep(1)
            exit()


def convert(x, y, turn):
    for i in vec:
        for j in vec:
            check_bool, endx, endy = put_check(x, y, i, j, turn)
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


def put_able_check(turn):
    put_able_cnt = 0
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == white or board[i][j] == black:
                continue
            
            for k in vec:
                for l in vec:
                    put_bool, tmp, tmp = put_check(i, j, k, l, turn)
                    if put_bool:
                        #print(i, j, k, l, put_bool)
                        board[i][j] = 2
                        put_able_cnt += 1
                        break
                else:
                    continue
                break
    return put_able_cnt


def put_check(x, y, vecx, vecy, turn):
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


def input_num():
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


def print_out():
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

def board_reset():
    global board
    board = [[0 for i in range(cell)]for j in range(cell)]
    board = np.array(board)
    board[3][4] = black
    board[4][3] = black
    board[3][3] = white
    board[4][4] = white

if __name__ == '__main__':
    main(start_turn)
