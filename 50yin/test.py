# 导入库
import pygame
from pygame.locals import *
import PIL

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
x1 = y1 = x2 = y2 = 0

screen.blit(lo, (0, 0))


def draw_screen(x1, y1, x2, y2, drawX, drawY):
    if x2 == y2 == 0:
        pass
    else:
        moveX = x2 - x1
        moveY = y2 - y1
        drawX += 0
        drawY += moveY
        if drawY < height - lo.get_height():
            drawY = height - lo.get_height()
        elif drawY > 0:
            drawY = 0
        x1 = y1 = x2 = y2 = 0
        screen.blit(lo, [drawX, drawY])


while True:
    event = pygame.event.wait()
    draw_screen(x1, y1, x2, y2, drawX, drawY)
    pygame.display.flip()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        x1, y1 = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        x2, y2 = pygame.mouse.get_pos()
