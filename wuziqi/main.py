# 导入库
import pygame
from pygame.locals import *
from screen import *
from wuziqi_logic import *
# 初始化Pygame
pygame.init()
# 绘制棋盘底部
draw_board_base()
# 默认黑棋先走 0黑 1白
blackorwhite = 0


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
            i, j = getij_fromposXY(posX, posY)
            if isCanPutdown(i, j):
                draw_chessman(blackorwhite, i, j)
                row_win, col_win, oblique_win, highlight_chess_list = analy_chess(
                    chess_book, i, j, blackorwhite)
                if isWin(row_win, col_win, oblique_win):
                    draw_hightlight_chess(highlight_chess_list)
                    if blackorwhite == 0:
                        print('黑棋获胜！')
                    else:
                        print('白棋获胜！')
                else:
                    blackorwhite = changehand(blackorwhite)
            else:
                pass
