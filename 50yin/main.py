# 导入库
import pygame
from pygame.locals import *
from screen import *

# 初始化Pygame
pygame.init()
screen = 'main'

while 1:
    # 绘制主场景
    draw_screen(screen)
    # 更新屏幕
    pygame.display.flip()
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            if btn_1_rect.collidepoint(posX, posY):
                screen = 'game'
            else:
                screen = 'main'
                print('n')
