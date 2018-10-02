import random
import pygame


"""游戏精灵类"""

# 屏幕大小的常量
# (x,y,width,height)
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """游戏角色"""
    def __init__(self,image_name,speed=1):
        """默认初始化精灵类."""
        super().__init__();
        self.image = pygame.image.load(image_name) #加载背景图片
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """更新精灵,默认存在移速在竖直方向."""
        self.rect.y +=self.speed # 先下移动.


class BackGround(GameSprite):
    """背景精灵"""
    def __init__(self,alt=False,image="./images/background.png"):
        super().__init__(image)
        if alt:
            #两张图片轮播,第二张图片需要在第一张图片上方,
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        #越界检查,如果移出边界,立即移动到替换图片位置
        if self.rect.y > SCREEN_RECT.height:
            self.rect.bottom = 0


class Hero(GameSprite):
    """英雄飞机"""
    def __init__(self):
        # 1. 调用父类方法，设置image&speed,因为英雄飞机是水平移动,所以该speed需要设置成0
        super().__init__("./images/me1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx  # 通过rect的中心直接获得.
        self.rect.bottom = SCREEN_RECT.bottom - self.rect.height #获得y的中心值

        self.bullets = pygame.sprite.Group() # 定义子弹的精灵组.

    def update(self):
        # 飞机的speed是指示左右移动的速度.
        self.rect.x += self.speed  # 默认右移
        # 越界检查
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > (SCREEN_RECT.width - self.rect.width):
            self.rect.x = SCREEN_RECT.width - self.rect.width
    def __del__(self):
        print("英雄飞机被销毁...")

    def shoot(self):
        # bullet = Bullet()
        # bullet.rect.x = self.rect.centerx
        # bullet.rect.y = self.rect.y
        # self.bullets.add(bullet)
        # 一次发射多发子弹
        for i in (0,1):
            bullet = Bullet()
            bullet.rect.x = self.rect.centerx
            bullet.rect.y = (self.rect.y - i*20) # 设置子弹的初始位置.
            self.bullets.add(bullet)


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1,3)
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x) # 设置随机X坐标
        # self.rect.y = - self.rect.height
        self.rect.bottom = 0 # 设置当前精灵的底部坐标. 会自动计算.
    def update(self):
        super().update()
        # 越界检查
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("敌机被销毁...")
        pass


class Bullet(GameSprite):
    """子弹类"""
    def __init__(self):
        super().__init__("./images/bullet1.png",-3)

    def update(self):
        super().update()
        if self.rect.y < 0:
            self.kill()
    def __del__(self):
        # print("子弹杯消灭...")
        pass