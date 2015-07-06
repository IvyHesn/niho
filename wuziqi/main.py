# 导入库
import pygame
from pygame.locals import *
from screen import *

# 初始化Pygame
pygame.init()
# 绘制棋盘底部
draw_board_base()
# 默认黑棋先走 0黑 1白
chessman = 0
chess_book = [[0] * 9] * 9
print (chess_book)
while 1:
     # 更新屏幕
    pygame.display.flip()
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            if isCanPutdown(posX, posY):
                draw_chessman(chessman, posX, posY)
                chessman = changehand(chessman)
            else:
                pass
