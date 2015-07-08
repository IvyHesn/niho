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
screen_type = 'game_ing'
# pygame.font.init()
font_list = pygame.font.get_fonts()
my_font = pygame.font.Font('./font/msyh.ttf', 32)


def doInScreen(screen_type):
    if screen_type == 'game_ing':
        pass
    if screen_type == 'game_end':
        pass


while 1:
     # 更新屏幕
    pygame.display.flip()
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if screen_type == 'game_ing':
            if event.type == pygame.MOUSEBUTTONDOWN:
                posX, posY = pygame.mouse.get_pos()
                i, j = getij_fromposXY(posX, posY)
                if isCanPutdown(i, j):
                    draw_chessman(blackorwhite, i, j)
                    row_win, col_win, oblique_win, highlight_chess_list = analy_chess(
                        chess_book, i, j, blackorwhite)
                    if isWin(row_win, col_win, oblique_win):
                        draw_hightlight_chess(highlight_chess_list)
                        chess_book = init_screen()
                        win_words(my_font, blackorwhite)
                        screen_type = 'game_end'
                    else:
                        blackorwhite = changehand(blackorwhite)
                else:
                    pass
        if screen_type == 'game_end':
            print(pygame.event.get())
            if event.type == pygame.MOUSEBUTTONDOWN:
                posX, posY = pygame.mouse.get_pos()
                if posX > 0:
                    #draw_board_base()
                    screen_type = 'game_ing'
                    pygame.display.update()
