# 导入库
import pygame
from pygame.locals import *
from screen import *

# 初始化Pygame
pygame.init()

while 1:
    # 绘图前，把屏幕填充为黑色
    screen.fill(0)
    # 绘制主场景
    screen_main()
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
                screen_game()
            else:
                print ('n')
