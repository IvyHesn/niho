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

lo = pygame.image.load('res/ui/lo.png')
drawX = 0
drawY = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0


def draw_sceen(drawX, drawY):
    screen.blit(lo, [drawX, drawY])

while 1:
    draw_sceen(drawX, drawY)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            x2, y2 = pygame.mouse.get_pos()
        moveX = x2 - x1
        moveY = y2 - y1
        drawX = drawX + moveX
        drawY = drawY + moveY
