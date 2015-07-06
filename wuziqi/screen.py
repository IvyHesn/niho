# 导入库
import pygame
from pygame.locals import *
import os

# 设置显示窗口
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
game_icon = pygame.image.load('res/game_icon.png')
pygame.display.set_icon(game_icon)
screen.fill((255, 255, 255))
pygame.display.set_caption('五子棋-无禁手')

# 导入图片
board_base = pygame.image.load('res/board_base.png')
chessman_black = pygame.image.load('res/chessman_black.png')
chessman_white = pygame.image.load('res/chessman_white.png')
chess_book = [[None for col in range(0, 15)]for row in range(0, 15)]
# 生成每个图片的位置
#btn_1_rect = pygame.Rect(228, 100, btn_1.get_width(), btn_1.get_height())
#btn_2_rect = pygame.Rect(228, 300, btn_1.get_width(), btn_1.get_height())
#btn_3_rect = pygame.Rect(228, 500, btn_1.get_width(), btn_1.get_height())


def draw_board_base():
    '''棋盘底'''
    for i in range(0, 15):
        for j in range(0, 15):
            screen.blit(board_base, [75 + i * 50, 75 + j * 50])


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
    '''判断落子后是否获胜'''
    row_win = [None] * 5
    col_win = [None] * 5
    oblique_win = [None] * 5
    for c in range(0, 5):
        if chess_book[i + c - 4][j] == chess_book[i + c - 3][j] == chess_book[i + c - 2][j] == chess_book[i + c - 1][j] == chess_book[i + c - 0][j] == blackorwhite:
            row_win[c] = 1
        else:
            row_win[c] = 0
    for c in range(0, 5):
        if chess_book[i][j + c - 4] == chess_book[i][j + c - 3] == chess_book[i][j + c - 2] == chess_book[i][j + c - 1] == chess_book[i][j + c - 0] == blackorwhite:
            col_win[c] = 1
        else:
            col_win[c] = 0
    for c in range(0, 5):
        if chess_book[i + c - 4][j + c - 4] == chess_book[i + c - 3][j + c - 3] == chess_book[i + c - 2][j + c - 2] == chess_book[i + c - 1][j + c - 1] == chess_book[i + c - 0][j + c - 0] == blackorwhite:
            oblique_win[c] = 1
        else:
            oblique_win[c] = 0
    print(row_win, col_win, oblique_win)
    if 1 in row_win + col_win + oblique_win:
        return True
    else:
        return False


def getij_fromposXY(posX, posY):
    if 75 <= posX <= 900 - 75 and 75 <= posY <= 900 - 75:
        i = (posX - 75) // 50
        j = (posY - 75) // 50
        return i, j
    else:
        return -1, -1


def draw_chessman(blackorwhite, i, j):
    '''绘制棋子，并加入棋谱'''
    if blackorwhite == 0:
        screen.blit(chessman_black, [i * 50 + 75 + 7.5, j * 50 + 75 + 7.5])
    elif blackorwhite == 1:
        screen.blit(chessman_white, [i * 50 + 75 + 7.5, j * 50 + 75 + 7.5])
    print(i, j)
    chess_book[i][j] = blackorwhite
    print(chess_book)


def changehand(blackorwhite):
    '''更换出手方'''
    blackorwhite = 1 - blackorwhite
    return blackorwhite
