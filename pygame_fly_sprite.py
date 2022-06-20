import random
import pygame

SCREEN_RECT = pygame.Rect((0, 0, 480, 700))
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class FlySprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    # 重写了sprite的update方法
    def update(self, *args):
        self.rect.y += self.speed


class BackGround(FlySprite):
    def __init__(self, is_alt, image_name, speed=1):
        super().__init__(image_name, speed)
        self.is_alt = is_alt
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

# 游戏启动后，每隔一秒出现一个敌机
# 速度是随机数
# 起始位置x坐标是随机数
# 敌机从屏幕下方飞出，不会再飞回屏幕（销毁对象）

# 创建定时器：pygame.time.set_timer(eventid, milliseconds)
# eventid是自定义的事件名
# 监听定时器事件：在pygame.event.get()可以获取到所有的事件列表，判断如果事件type == eventid，说明定时器事件发生
class Enemy(FlySprite):
    def __init__(self, speed = 1):
        # 指定图片、设置初始位置和初始速度
        super().__init__('./images/enemy1.png')
        self.speed = random.randint(1, 3)
        # self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # 避免内存浪费
            print('敌机飞出屏幕了')
            self.kill()  # sprint类中的方法

# 学习目标：
# 设计英雄和子弹类
# 使用键盘移动英雄
# 发射子弹
# 碰撞实现


class Hero(FlySprite):
    def __init__(self):
        super().__init__('./images/me1.png')
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullets_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (1,2,3):
            bullet1 = Bullet()
            bullet1.rect.centerx = self.rect.centerx
            bullet1.rect.y = self.rect.y - 20 * i
            self.bullets_group.add(bullet1)
        print('发射子弹...')


# 指定图片和初始速度
# update方法啊，判断是否废除屏幕，如果是，从精灵组删除
class Bullet(FlySprite):
    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill
