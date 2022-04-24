import copy
import random
import numpy as np

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
        board = osero.convert(li[0], li[1], turn, board)
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

def cpu_table(board_org, turn):
    board = copy.deepcopy(board_org)
    put_able_list = []
    for i in range(cell):
        for j in range(cell):
            if board[i][j] == 2:
                put_able_list.append([i, j])
    put_able_cnt_min = 64
    table = np.load("black_table.npy")
    alpha = 1
    for li in put_able_list:
        score = 0
        board = copy.deepcopy(board_org)
        board = osero.convert(li[0], li[1], turn, board)
        put_able_cnt, tmp = osero.put_able_check(turn * -1, board)
        score = alpha * table[li[0]][li[1]] - put_able_cnt
        print(li, score)
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

def cpu_deep(board_org, turn, deep_max = 5):
    def get_put_list(board, deep):
        put_able_list = []
        for i in range(cell):
            for j in range(cell):
                if board[i][j] == 2:
                    put_able_list.append([i, j, deep, copy.deepcopy(board)])
        return put_able_list

    forbid_grid = [[0,1],[1,0],[1,1],[0,6],[1,6],[1,7],[6,0],[6,1],[7,1],[6,6],[6,7],[7,6]]

    board = copy.deepcopy(board_org)
    put_able_list = get_put_list(board, 0)
    put_able_cnt_min = 64
    for li in put_able_list:
        score = 0
        deep = 0
        board = copy.deepcopy(board_org)

        dfs = [[li[0], li[1], deep, board]]
        while dfs != []:
            tmp = dfs.pop(0)
            deep = tmp[2]
            if deep > deep_max:
                continue
            board = tmp[3]

            board = osero.convert(tmp[0], tmp[1], turn * (-1)**deep, board)
            deep += 1
            put_able_cnt, board = osero.put_able_check(turn * (-1)**deep, board)
            if turn * (-1)**deep == turn:
                score -= put_able_cnt
            else:
                score += put_able_cnt
            dfs = dfs + get_put_list(board, deep)
            if [tmp[0], tmp[1]] in forbid_grid:
                score += 10
        
        print(li[:2], put_able_cnt)
        if li[:2] in forbid_grid:
            score += 10
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


class q_learning():
    def new_table():
        table = np.zeros((64, 3 ** 8))
        for i in range(8):
            s = i * 8 + 1
            e = s + 7
            filename = "qtable/qtable_" + str(s) + "-" + str(e) + ".npy"
            np.save(filename, table)
    def load_table(start):
        filename = "qtable/qtable_" + str(start) + "-" + str(start + 7) + ".npy"
        table = np.load(filename)
        return table

    def save_table(start, table):
        filename = "qtable/qtable_" + str(start) + "-" + str(start + 7) + ".npy"
        np.save(filename, table)

    def computer(board):
        np.load()
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


