#coding=utf-8

import pygame
from pygame.locals import *
from HeroPlane import HeroPlane
from EnemyPlane import EnemyPlane
"""
    游戏入口.
"""





if __name__ == "__main__":
    # sys.path.append(".")
    #1.创建一个主界面.
    screen = pygame.display.set_mode((480,890),0,32)
    #2.创建背景图片
    background = pygame.image.load("./image/background.png").convert()

    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    # bullet = Bullet(screen,30,30)
    #3.显示
    while True:
        # 初始化主界面.
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        # 监听键盘.  无法实现按着不放,实现快速移动.
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    hero.heromoveleft()
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    hero.heromoveright()
                elif event.key == K_SPACE:
                    print("space")
                    hero.shoot()
        # 刷新画布.
        pygame.display.update()
