# 导入库
import pygame
from pygame.locals import *
import os

# 设置显示窗口
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.display.set_caption('五子棋')

# 导入图片
board_base = pygame.image.load('res/board_base.png')
chessman_black = pygame.image.load('res/chessman_black.png')
chessman_white = pygame.image.load('res/chessman_white.png')

# 生成每个图片的位置
#btn_1_rect = pygame.Rect(228, 100, btn_1.get_width(), btn_1.get_height())
#btn_2_rect = pygame.Rect(228, 300, btn_1.get_width(), btn_1.get_height())
#btn_3_rect = pygame.Rect(228, 500, btn_1.get_width(), btn_1.get_height())


def draw_board_base():
    '''棋盘底'''
    for i in range(0, 15):
        for j in range(0, 15):
            screen.blit(board_base, [75 + i * 50, 75 + j * 50])


def isCanPutdown(x, y):
    '''判断棋子是否可以被放下'''
    pass
    return True


def draw_chessman(chessman, x, y):
    '''绘制棋子，并加入棋谱'''
    if chessman == 0:
        screen.blit(chessman_black, [x, y])
    elif chessman == 1:
        screen.blit(chessman_white, [x, y])


def changehand(chessman):
    '''更换出手方'''
    chessman = 1 - chessman
    return chessman
