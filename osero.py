#*- coding:utf-8 -*-
#!/bin/python3
import sys
import numpy as np

cell = 8

white = -1
blank = 0
black = 1

count = -1

cheak = False

reve_count = 0
tmp = [-1, 0, 1]

board = [[0 for i in range(cell)]for j in range(cell)]
board = np.array(board)
board[3][4] = white
board[4][3] = white
board[3][3] = black
board[4][4] = black

#board[0] = [1,1,1,1,1,1,1,1]
#board[1] = [1,1,-1,1,1,1,1,1]
#board[2] = [1,1,1,1,1,1,1,1]
#board[3] = [1,1,1,1,1,1,1,1]
#board[4] = [1,1,1,1,1,1,1,1]
#board[5] = [1,1,1,1,1,1,1,1]
#board[6] = [1,1,1,1,1,1,1,1]
#board[7] = [1,0,0,-1,1,1,1,1]

#board[2][3] = black
#board[2][2] = black
#board[4][4] = white
#board[3][1] = white


def turn():
    global count
    if count == white:
        print("turn : white")
    if count == black:
        print("turn : black")
    #print(input_num())
    x, y = input_num()
    if x != -1:
        board[x][y] = count
        for i in tmp:
            for j in tmp:
                global reve_count
                reve_count = 0
                cheak2(x, y, i, j)
    print_out()
#    print(0 in board[0])
    if (0 in board):
        count *= (-1)
        turn()
    else:
        white_num = 0
        black_num = 0
        #for i in range(cell):
        #    white_num = white_num + board[i].count(white)
        #    black_num = black_num + board[i].count(black)
        #white_num = board[0].count(white)
        #black_num = board[0].count(black)
        white_num = np.count_nonzero(board == white)
        black_num = np.count_nonzero(board == black)
        print("white : " + str(white_num) + "   black : " + str(black_num))
        if white_num == black_num:
            print("draw")
            exit()
        elif white_num > black_num:
            print("win white")
            exit()
        elif white_num < black_num:
            print("win black")
            exit()


def _cheak(x, y):
    global cheak
    global count
    global reve_count
    cheak = False 
    for i in tmp:
        for j in tmp:
            reve_count = 0
            cheak = cheak_ij(x,y,i,j)
            if cheak == True:
                break
        else:
            cheak = False
            continue
        break
    #print("cheak = " + str(cheak))
    return cheak


def cheak_ij(x,y,i,j):
    global cheak
    global count
    global reve_count
    #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
    if 0 <= x - i <= 7 and 0 <= y -j <= 7:
        if reve_count == 0:
            if board[x - i][y - j] == count*(-1):
                reve_count += 1
                #print("1-1")
                #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
                chaek = cheak_ij(x-i, y-j, i ,j)
            else :
                cheak = False
                #print("1-2")
                #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
        else:
            if board[x - i][y - j] == count*(-1):
                reve_count += 1
                #print("2-1")
                #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
                cheak = cheak_ij(x-i, y-j, i, j)
            elif board[x - i][y - j] == count:
                cheak = True
                #print("2-2")
                #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
            else :
                cheak = False
                #print("2-3")
                #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
    else:
        cheak = False
        #print("x : " + str(x) + "  y : " + str(y) + "  i : " + str(i)+ " j : " + str(j))
    #print(cheak)
    return cheak

#def cheak(x, y, i, j):
#    global cheak
#    global count
#    global reve_count
#    if 0 <= x - i <= 7 and 0 <= y -j <= 7:
#        if reve_count == 0:
#            if board[x - i][y - j] == count*(-1):
#                reve_count += 1
#                chaek =  cheak(x-i, y-j, i, j)
#            else :
#                cheak = False
#        else:
#            if board[x - i][y - j] == count*(-1):
#                reve_count += 1
#                cheak = cheak(x-i, y-j, i, j)
#            elif board[x - i][y - j] == count:
#                cheak = True
#            else :
#                cheak = False
#    else :
#        cheak = False
#    
#    return cheak


def cheak2(x, y, i, j):
    global count
    global reve_count
    if 0 <= x - i <= 7 and 0 <= y -j <= 7:
        if reve_count == 0:
            if board[x - i][y - j] == count*(-1):
                reve_count += 1
                cheak2(x-i, y-j, i, j)
        else:
            if board[x - i][y - j] == count*(-1):
                reve_count += 1
                cheak2(x-i, y-j, i, j)
            elif board[x - i][y - j] == count:
                for k in range(reve_count):
                    convert(x+(k*i), y+(k*j))
    
#def cheak(x, y, i, j):
#    global count
#    global reve_count
#    if board[x - i][y - j] == count*(-1):
#        reve_count += 1
#        cheak2(x-i, y-j, i, j)
#
#
#def cheak2(x, y, i, j, aaa):
#    global count
#    global reve_count
#    if board[x - i][y - j] == count*(-1):
#        reve_count += 1
#        cheak2(x-i, y-j, i, j)
#    elif board[x - i][y - j] == count:
#        #print(reve_count)
#            for k in range(reve_count):
#                #print(str(x+(k*i)) + "  " + str(y+(k*j)))
#                convert(x+(k*i), y+(k*j))


def convert(x,y):
    board[x][y] = board[x][y]*(-1)


#def input_num2():
#    while True:
#        x,y = 0,0
#        print("while")
#        x, y = map(int, input().split())
#        if  x < 0 or 7 < x or y < 0 or 7 < y:
#            print("x and y is 0~7")
#        else :
#            if board[x][y] != 0:
#                print("already storne")
#            else :
#                print("YES")
#                #print("sample = " + str(x) + " " + str(y))
#                a = _cheak(x,y)
#                #print(a)
#                if a == True:
#                    break
#                else:
#                    print("no put")
#    print(str(x) + " " + str(y))
#    return x, y



def input_num():
    while True:
        x,y = 0,0
        a = 0
        try:
            x, y = map(int, input().split())
            if x == -1 and y == -1:
                break
            elif  x < 0 or 7 < x or y < 0 or 7 < y and x != -1 and y != -1:
                print("x and y is 0~7")
            else :
                if board[x][y] != 0:
                    print("already storne")
                else :
                    #print("YES")
                    #print("sample = " + str(x) + " " + str(y))
                    a = _cheak(x,y)
                    if a == True:
                        break
                    else:
                        print("no put")
        except (TypeError, ValueError):
        #except ValueError:
            print("again")
            pass
    #print(str(x) + " " + str(y))
    return x, y

#def input_num():
#    global cheak
#    x, y = map(int, input().split())
#        if  x < 0 or 7 < x or y < 0 or 7 < y:
#            print("x and y is 0~7")
#            x, y = input_num()
#        else :
#            if board[x][y] != 0:
#                print("already storne")
#                x, y = input_num()
#    else :
#        x, y = input_num()
#    return x, y


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
            else :
                print("   ", end="|")
        print("")
        print("ーーーーーーーーーーーーーーーーー")


if __name__ == '__main__':
    print_out()
    turn()
