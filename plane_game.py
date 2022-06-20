# 面向对象写法 飞机大战
import pygame
from pygame_fly_sprite import *


class PlaneGame:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        self.__createSprite()

    # 创建精灵
    def __createSprite(self):
        # self.hero_group = pygame.sprite.Group()
        bg1 = BackGround(False, './images/background.png')
        bg2 = BackGround(True, './images/background.png')
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 事件监听
    def start_game(self):
        print('开始游戏...')
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collides()
            self.__update_sprites()
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        press_keys = pygame.key.get_pressed()
        if press_keys[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif press_keys[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collides(self):
        pygame.sprite.groupcollide(self.hero.bullets_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            self.__game_over()
        pass

    # 更新精灵组 包含背景、英雄、敌机
    def __update_sprites(self):
        # for group in [self.back_group,  self.hero_group,self.enemy_group]:x
        for group in [self.back_group, self.enemy_group, self.hero_group, self.hero.bullets_group]:
            group.update()
            group.draw(self.screen)

    def __game_over(self):
        pygame.quit()
        exit()


game = PlaneGame()
game.start_game()
