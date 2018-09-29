#coding=utf-8
import pygame
from Bullet import Bullet
"""
    玩家飞机类.

"""

class HeroPlane(object):

    def __init__(self,screen):
        #初始位置
        self.x = 230
        self.y = 600
        self.screen = screen
        self.imageName = "./image/hero.gif"
        self.image = pygame.image.load(self.imageName).convert()

        self.bullets = []

    def display(self):
        # 显示hero飞机
        # 判断飞机是否爆炸
        self.screen.blit(self.image,(self.x,self.y))
        # 显示子弹.
        # print(len(self.bullets))
        for bullet in self.bullets:
            if bullet.y < 0:
                self.bullets.pop(0)
            bullet.display()
            bullet.move()

    def heromoveleft(self):
        self.x -= 10
        if self.x < -50:
            self.x = -50
    def heromoveright(self):
        self.x += 10
        if self.x > 430:
            self.x = 430
    def shoot(self):
        b = Bullet(self.screen,self.x+45,self.y,2)
        self.bullets.append(b)

