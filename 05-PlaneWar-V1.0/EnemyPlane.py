#coding=utf-8
import pygame
import random
from Bullet import Bullet
"""
    敌机
"""

class EnemyPlane(object):

    def __init__(self,screen):
        #初始位置
        self.x = random.randint(20,450)
        self.y = 1
        self.screen = screen
        self.imageName = "./image/enemy-1.gif"
        self.image = pygame.image.load(self.imageName).convert()
        self.redirect = "left"
        self.bullets = []
        self.count = 1
    def display(self):
        print("当前敌机子弹:" + str(len(self.bullets)))
        self.count +=1
        if self.count > 10000:
            self.count = 1
        if random.randint(1,1000) == 50:
            self.shoot()
        if self.count%10 == 0:
            self.move()
        self.screen.blit(self.image,(self.x,self.y));
        for bullet in self.bullets:
            if bullet.y > 890:
                self.bullets.pop(0)
            bullet.display()
            bullet.move()

    def move(self):
        # 默认不让左右移动
        if self.redirect == "left":
            self.x -=3
            if self.x <= 10:
                self.redirect = "right"
        if self.redirect == "right":
            self.x +=3
            if self.x > 450:
                self.redirect = "left"

    def shoot(self):
        b = Bullet(self.screen,self.x+45,self.y,1)
        self.bullets.append(b)