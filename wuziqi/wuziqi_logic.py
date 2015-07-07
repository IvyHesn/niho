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


def analy_chess(chess_book, i, j, blackorwhite):
    '''解析盘面，返回致胜格子列表'''
    row_win = [None] * 5
    col_win = [None] * 5
    oblique_win = [None] * 5
    highlight_chess_list = []
    for c in range(0, 5):
        row_win_cmp = [None] * 5
        if 0 <= i + c - 4 and i + c - 0 < 15:
            for c2 in range(0, 5):
                if chess_book[i + c - 4][j] == chess_book[i + c - 4 + c2][j] == blackorwhite:
                    row_win_cmp[c2] = 1
                    if row_win_cmp == [1, 1, 1, 1, 1]:
                        row_win[c] = 1
                        add_highlight1 = [
                            [i + c - 4, j], [i + c - 3, j], [i + c - 2, j], [i + c - 1, j], [i + c, j]]
                        highlight_chess_list.extend(add_highlight1)
    for c in range(0, 5):
        col_win_cmp = [None] * 5
        if 0 <= j + c - 4 and j + c - 0 < 15:
            for c2 in range(0, 5):
                if chess_book[i][j + c - 4] == chess_book[i][j + c - 4 + c2] == blackorwhite:
                    col_win_cmp[c2] = 1
                    if col_win_cmp == [1, 1, 1, 1, 1]:
                        col_win[c] = 1
                        add_highlight2 = [
                            [i, j + c - 4], [i, j + c - 3], [i, j + c - 2], [i, j + c - 1], [i, j + c]]
                        highlight_chess_list.extend(add_highlight2)
    for c in range(0, 5):
        oblique_win_cmp = [None] * 5
        if 0 <= i + c - 4 and 0 <= j + c - 4 and i + c - 0 < 15 and j + c - 0 < 15:
            for c2 in range(0, 5):
                if chess_book[i + c - 4][j + c - 4] == chess_book[i + c - 4 + c2][j + c - 4 + c2] == blackorwhite:
                    oblique_win_cmp[c2] = 1
                    if oblique_win_cmp == [1, 1, 1, 1, 1]:
                        oblique_win[c] = 1
                        add_highlight3 = [
                            [i + c - 4, j + c - 4], [i + c - 3, j + c - 3], [i + c - 2, j + c - 2], [i + c - 1, j + c - 1], [i + c, j + c]]
                        highlight_chess_list.extend(add_highlight3)
    #print(row_win, col_win, oblique_win)
    # print(highlight_chess_list)
    return row_win, col_win, oblique_win, highlight_chess_list


def isWin(row_win, col_win, oblique_win):
    '''判断落子后是否获胜'''
    if 1 in row_win + col_win + oblique_win:
        return True
    else:
        return False
