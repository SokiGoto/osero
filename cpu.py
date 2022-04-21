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
    put_able_cnt_min = 64
    for li in put_able_list:
        board = copy.deepcopy(board_org)
        board_after = osero.convert(li[0], li[1], turn, board)
        put_able_cnt, tmp = osero.put_able_check(turn * -1, board)
        print(li, put_able_cnt)
        if put_able_cnt_min > put_able_cnt:
            put_list = [li]
            put_able_cnt_min = put_able_cnt
        elif put_able_cnt_min == put_able_cnt:
            put_list.append(li)
    
    tmp = random.randint(0, len(put_list)-1)
    x = put_list[tmp][0]
    y = put_list[tmp][1]

    print("put", x, y)
    return x, y

def cpu_weak_forbid(board_org, turn):
    forbid_grid = [[0,1],[1,0],[1,1],[0,6],[1,6],[1,7],[6,0],[6,1],[7,1],[6,6],[6,7],[7,6]]

    board = copy.deepcopy(board_org)
    put_able_list = []
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == 2:
                put_able_list.append([i, j])
    put_able_cnt_min = 64
    for li in put_able_list:
        board = copy.deepcopy(board_org)
        board_after = osero.convert(li[0], li[1], turn, board)
        put_able_cnt, tmp = osero.put_able_check(turn * -1, board)
        if li in forbid_grid:
            put_able_cnt += 10
        print(li, put_able_cnt)
        if put_able_cnt_min > put_able_cnt:
            put_list = [li]
            put_able_cnt_min = put_able_cnt
        elif put_able_cnt_min == put_able_cnt:
            put_list.append(li)

    tmp = random.randint(0, len(put_list)-1)
    x = put_list[tmp][0]
    y = put_list[tmp][1]

    print("put", x, y)
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


