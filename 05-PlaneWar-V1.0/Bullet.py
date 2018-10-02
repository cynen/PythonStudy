#coding=utf-8
import pygame
"""
    子弹类.
"""


class Bullet(object):
    def __init__(self,screen,x,y,type):
        self.x = x
        self.y = y
        self.screen = screen
        self.type = type
        if self.type == 1:
            self.image = pygame.image.load("./image/bullet-1.gif")
        # elif self.type == 2:
        #     self.image = pygame.image.load("./image/bullet-2.gif").convert()
        elif self.type == 2:
            self.image = pygame.image.load("./image/bullet-3.gif")

        self.count = 1
    def move(self):
        self.count += 1
        if self.count > 10000:  #单线程的弊端...为了延缓子弹的移速.
            self.count = 1
        #每个子弹有自己的移动
        if self.count % 2 == 0: #减速一半.
            if self.type == 1:
                self.y +=1
            elif self.type == 2:
                self.y -=1

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
