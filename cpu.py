import copy
import random

import osero

cell = osero.cell
vec = osero.vec

blank = osero.blank
black = osero.black
white = osero.white

def cpu(board):
    max_deep = 3
    deep = 0
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == 2:
                put_able_list.pop([i, j])
    x = put_able_list[0][0]
    y = put_able_list[0][1]
    for i in put_able_list:
        dfs = []

def cpu_weak(board_org, turn):
    board = copy.deepcopy(board_org)
    put_able_list = []
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == 2:
                put_able_list.append([i, j])
    x = put_able_list[0][0]
    y = put_able_list[0][1]
    print("befor", x, y)
    put_able_cnt_min = 64
    for li in put_able_list:
        board = copy.deepcopy(board_org)
        board_after = convert(li[0], li[1], board, turn)
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
        #print_out(board_after)
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        put_able_cnt = put_able_check(turn * -1, board)
        print(li,put_able_cnt)
        if put_able_cnt_min > put_able_cnt:
            put_able_cnt_min = put_able_cnt
            x = li[0]
            y = li[1]

    print("after", x, y)
    return x, y

def cpu_random(board):
    put_able_list = []
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == 2:
                put_able_list.append([i, j])
    tmp = random.randint(0, len(put_able_list)-1)
    return put_able_list[tmp][0], put_able_list[tmp][1]


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

def convert(x, y, board, turn):
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
    return put_able_cnt


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
