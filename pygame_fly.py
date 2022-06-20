# Day11
# 面向过程写法
import pygame
from pygame_fly_sprite import *

pygame.init()
screen = pygame.display.set_mode((480, 700))
pygame.display.set_caption('飞机大战')

bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (150, 300))
pygame.display.update()
hero_rect = pygame.Rect(150, 300, 102, 126)

clock = pygame.time.Clock()

enemy1 = FlySprite('./images/enemy1.png')
enemy2 = FlySprite('./images/enemy1.png', 2)
enemy3 = FlySprite('./images/enemy1.png', 3)
enemy4 = FlySprite('./images/enemy1.png', 4)

enemy2.rect.x = 200
enemy3.rect.x = 300
enemy4.rect.x = 400
enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
pygame.quit()
