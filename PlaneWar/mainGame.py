
import pygame
from pygame.locals import *
import sys



SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('飞机大战')


# 载入背景图
background = pygame.image.load('./image/background.png').convert()
#game_over = pygame.image.load('./image/gameover.png')

filename = './image/shoot.png'
plane_img = pygame.image.load(filename)

clock = pygame.time.Clock()

while 1:
    # 控制游戏最大帧率为60
    clock.tick(60)
    # 绘制背景
    screen.fill(0)
    screen.blit(background, (0, 0))

    #添加图片:
    screen.blit(1,())



    # 更新屏幕
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()