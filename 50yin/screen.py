# 导入库
import pygame
from pygame.locals import *
import os

# 设置显示窗口
width, height = 640, 960
screen = pygame.display.set_mode((width, height))

# 导入图片
btn_1 = pygame.image.load('res/ui/btn_1.png')
btn_2 = pygame.image.load('res/ui/btn_2.png')
btn_3 = pygame.image.load('res/ui/btn_3.png')

# 生成每个图片的位置
btn_1_rect = pygame.Rect(228, 100, btn_1.get_width(), btn_1.get_height())
btn_2_rect = pygame.Rect(228, 300, btn_1.get_width(), btn_1.get_height())
btn_3_rect = pygame.Rect(228, 500, btn_1.get_width(), btn_1.get_height())


def screen_main():
    '''主场景'''
    screen.blit(btn_1, [228, 100])
    screen.blit(btn_1, [228, 300])
    screen.blit(btn_1, [228, 500])


def screen_game():
    '''游戏类'''
    screen.blit(btn_2, [228, 100])
    screen.blit(btn_3, [228, 300])
    screen.blit(btn_1, [228, 500])
