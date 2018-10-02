import time
import pygame
from GameRole import *

"""飞机大战 V2.0版本"""

class PlaneGame(object):
    def __init__(self):
        """初始化游戏"""
        print("初始化游戏...")
        #1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建时钟对象
        self.clock = pygame.time.Clock()
        #3.创建游戏精灵
        self.__creat_sprites()
        #4.设置定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000) #1秒触发一个 CREATE_ENEMY_EVENT 事件.
        pygame.time.set_timer(HERO_FIRE_EVENT,500) #0.5秒触发一个 HERO_FIRE_EVENT事件.




    def __creat_sprites(self):
        """创建精灵"""
        #1.创建背景精灵组.
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.bgGroup = pygame.sprite.Group()
        self.bgGroup.add(bg1,bg2)

        #2.创建英雄飞机.
        self.hero = Hero()
        self.heroGroup = pygame.sprite.Group(self.hero)
        #3.创建敌机的Group ,具体的敌机,需要定时器事件去创建
        self.enemyGroup = pygame.sprite.Group()


    def __update_sprites(self):
        """更新游戏精灵,顺序决定了层次"""
        #更新背景精灵组
        self.bgGroup.update()
        self.bgGroup.draw(self.screen)
        # 更新敌机
        self.enemyGroup.update()
        self.enemyGroup.draw(self.screen)
        #更新飞机
        self.heroGroup.update()
        self.heroGroup.draw(self.screen)
        #更新子弹
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __check_collide(self):
        """碰撞检测"""
        # 子弹和敌机碰撞检测,2个精灵组都会消失.
        pygame.sprite.groupcollide(self.hero.bullets,self.enemyGroup,True,True)

        #英雄与敌机碰撞检测
        collideList = pygame.sprite.spritecollide(self.hero,self.enemyGroup,True)
        if collideList:
            self.hero.kill()
            PlaneGame.__game_over()

    def __event_handler(self):
        """事件监听."""
        for event in pygame.event.get():
            #1. 判断是否关闭了游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            #2. 判断定时器事件.
            elif event.type == CREATE_ENEMY_EVENT:
                # print("创建敌机")
                enmey = Enemy()
                self.enemyGroup.add(enmey)
            elif event.type == HERO_FIRE_EVENT:
                # print("开火事件.")
                self.hero.shoot()
            elif event.type == pygame.MOUSEBUTTONUP: # 松开鼠标左键.
                x,y = pygame.mouse.get_pos()
                print("当前位置:" + str(x) + str(y))
                print("按下了鼠标")
            # elif event.type == pygame.MOUSEMOTION: # 移动鼠标
            #     print("WOW")

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #手动射击.
            #     self.hero.shoot()
            #按键检测
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     # 飞机右移
            #     print("飞机右移")
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     #飞机左移
            #     print("飞机左移")

        # 持续按键检测
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]: # 持续检测是否按住了 左键.
            self.hero.speed = -2
        elif key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.hero.speed = 2
        else:
            self.hero.speed = 0

    def __bootcreat_sprites(self):
        """创建精灵"""
        #1.创建启动背景精灵组.
        bg1 = BackGround("./ui/bg00.jpg")
        bg2 = BackGround("./ui/bg00.jpg",True)
        self.bgGroup1 = pygame.sprite.Group()
        self.bgGroup1.add(bg1,bg2)


    def __bootupdate_sprites(self):
        """启动界面更新游戏精灵,顺序决定了层次"""
        #更新背景精灵组
        self.bgGroup.update()
        self.bgGroup.draw(self.screen)

    def __bootevent_handler(self):
        """启动界面事件监听."""
        for event in pygame.event.get():
            #1. 判断是否关闭了游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            if event.type == pygame.MOUSEBUTTONUP: # 松开鼠标左键.
                x,y = pygame.mouse.get_pos()
                print("当前位置:" + str(x) + str(y))
                if   100 <x< 200 and  100<y<200:
                    self.flag2 = False # 退出当前启动界面.
                    print("按下了鼠标")
            # elif event.type == pygame.MOUSEMOTION: # 移动鼠标
            #     print("WOW")



    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit(0)
    def start_game(self):
        print("开始游戏...")
        # 挖坑,后续待填!!!
        # self.flag2 = True
        # while self.flag2:
        # # self.bootGame()
        #     self.clock.tick(10)
        #     self.__bootevent_handler()
        #     # 4.更新精灵.
        #     self.__bootupdate_sprites()
        #     # 5.刷新画布
        #     pygame.display.update()
        #

        while True:
            #1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            #2.事件监听
            self.__event_handler()

            #3.碰撞检测
            self.__check_collide()

            #4.更新精灵.
            self.__update_sprites()

            #5.刷新画布
            pygame.display.update()

    def bootGame(self):
        """启动游戏界面,实验失败..."""
        bg = BackGround("./ui/bg00.jpg")
        self.bgGroup.add(bg)
        self.bgGroup.update()
        self.bgGroup.draw(self.screen)
        pygame.display.update()




if __name__ == '__main__':
    """主程序入口"""
    PlaneGame().start_game()



