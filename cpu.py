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
        board_after = osero.convert(li[0], li[1], turn, board)
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
        #print_out(board_after)
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        put_able_cnt, tmp = osero.put_able_check(turn * -1, board)
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
    if len(put_able_list) == 0:
        return  
    else:
        tmp = random.randint(0, len(put_able_list)-1)
        return put_able_list[tmp][0], put_able_list[tmp][1]


