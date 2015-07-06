from screen import *


def isCanPutdown(i, j):
    '''判断是否可以落子'''
    if 0 <= i < 15 and 0 <= j < 15:
        if chess_book[i][j] == None:
            return True
        else:
            print('不能在已有棋子的格子下棋！')
            return False
    else:
        print('不能在棋盘外下棋！')
        return False


def isWin(chess_book, i, j, blackorwhite):
    '''判断落子后是否获胜，并返回应该高亮的格子'''
    row_win = [None] * 5
    col_win = [None] * 5
    oblique_win = [None] * 5
    row_win_cmp = [None] * 5
    col_win_cmp = [None] * 5
    oblique_win_cmp = [None] * 5
    for c in range(0, 5):
        if 0 <= i + c - 4 and i + c - 0 < 15:
            for c2 in range(0, 5):
                if chess_book[i + c - 4][j] == chess_book[i + c - 4 + c2][j] == blackorwhite:
                    row_win[c] = 1
    for c in range(0, 5):
        if 0 <= j + c - 4 and j + c - 0 < 15:
            for c2 in range(0, 5):
                if chess_book[i][j + c - 4] == chess_book[i][j + c - 4 + c2] == blackorwhite:
                    col_win_cmp[c2] = 1
                    if col_win_cmp == [1, 1, 1, 1, 1]:
                        col_win[c] = 1
    for c in range(0, 5):
        if 0 <= i + c - 4 and 0 <= j + c - 4 and i + c - 0 < 15 and j + c - 0 < 15:
            for c2 in range(0, 5):
                if chess_book[i + c - 4][j + c - 4] == chess_book[i + c - 4 + c2][j + c - 4 + c2] == blackorwhite:
                    oblique_win_cmp[c2] = 1
                    if oblique_win_cmp == [1, 1, 1, 1, 1]:
                        oblique_win[c] = 1
    print(row_win, col_win, oblique_win)

    if 1 in row_win + col_win + oblique_win:
        return True
    else:
        return False
