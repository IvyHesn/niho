# 导入库
import pygame
from pygame.locals import *


# 初始化Pygame
pygame.init()
# 设置显示窗口
width, height = 640, 960
screen = pygame.display.set_mode((width, height))
screen.fill((223, 234, 236))
pygame.display.set_caption('web_ids')
pygame.display.flip()
lo = pygame.image.load('res/ui/lo.png')

screen.blit(lo, [0, 0])


while 1:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            moveX, moveY = pygame.mouse.get_rel()
            print (moveX,moveY)
            screen.blit(lo, [moveX, moveY])
