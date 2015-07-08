# 导入库
import pygame
from pygame.locals import *
import os
import time

# 设置显示窗口
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
game_icon = pygame.image.load('res/game_icon.png')
pygame.display.set_icon(game_icon)
screen.fill((255, 255, 191))
pygame.display.set_caption('五子棋-无禁手')

# 导入图片
board_base = pygame.image.load('res/board_base.png')
board_base_1 = pygame.image.load('res/board_base_1.png')
board_base_2 = pygame.image.load('res/board_base_2.png')
highlight_circle = pygame.image.load('res/highlight_circle.png')
chessman_black = pygame.image.load('res/chessman_black.png')
chessman_white = pygame.image.load('res/chessman_white.png')
# 生成每个图片的位置
# btn_1_rect = pygame.Rect(228, 100, btn_1.get_width(), btn_1.get_height())
# btn_2_rect = pygame.Rect(228, 300, btn_1.get_width(), btn_1.get_height())
# btn_3_rect = pygame.Rect(228, 500, btn_1.get_width(), btn_1.get_height())
# 字体


def init_screen():
    chess_book = [[None for col in range(0, 15)]for row in range(0, 15)]
    return chess_book
chess_book = init_screen()

def draw_board_base():
    '''绘制棋盘底'''
    for i in range(0, 15):
        for j in range(0, 15):
            if (i + j) % 2 == 0:
                screen.blit(board_base_1, [75 + i * 50, 75 + j * 50])
            else:
                screen.blit(board_base_2, [75 + i * 50, 75 + j * 50])


def getij_fromposXY(posX, posY):
    '''根据鼠标XY，得到落子点ij'''
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
    # print(i, j)
    chess_book[i][j] = blackorwhite
    # print(chess_book)




def changehand(blackorwhite):
    '''更换出手方'''
    blackorwhite = 1 - blackorwhite
    return blackorwhite


def draw_hightlight_chess(highlight_chess_list):
    '''高亮致胜棋子'''
    for grid in highlight_chess_list:
        screen.blit(
            highlight_circle, [grid[0] * 50 + 75 + 4.5, grid[1] * 50 + 75 + 4.5])
        pygame.display.update()
        screen.blit(
            highlight_circle, [grid[0] * 50 + 75 + 4.5, grid[1] * 50 + 75 + 4.5])
        pygame.display.update()
        screen.blit(
            highlight_circle, [grid[0] * 50 + 75 + 4.5, grid[1] * 50 + 75 + 4.5])
        pygame.display.update()


def win_words(my_font, blackorwhite):
    '''文字：宣布胜利方'''
    if blackorwhite == 0:
        font_win_surface_0 = my_font.render(
            r'黑棋获胜!', True, (0, 0, 0), (255, 255, 255))
        screen.blit(font_win_surface_0, (400, 450))
    else:
        font_win_surface_1 = my_font.render(
            r'白棋获胜!', True, (0, 0, 0), (255, 255, 255))
        screen.blit(font_win_surface_1, (400, 450))
