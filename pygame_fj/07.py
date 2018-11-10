import pygame
from python_jlz import *
#游戏初始化
pygame.init()
#创建游戏的窗口512*768
screen = pygame.display.set_mode((512,768))#返回suface
#绘制背景图像
bg = pygame.image.load('images/bg1.jpg')#加载背景
screen.blit(bg,(0,0))
#绘制英雄飞机
hero = pygame.image.load('images/hero1.png')
screen.blit(hero,(200,600))
pygame.display.update()

clock = pygame.time.Clock()
#1.定义rect纪录飞机初始位置
hero_rect = pygame.Rect(200,600,128,128)

#创建敌机的精灵
enemy = GameSprite("images/en1.png")
enemy1 = GameSprite("images/en1.png", 2)#传入speed参数2//默认参数是1。
#创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('game over')
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= -128:
        hero_rect.y = 768
    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)
    #让精灵组调用两个方法
    #update()让组中的所有精灵更新位置
    enemy_group.update()
    #draw()在screen上绘制所有的精灵
    enemy_group.draw(screen)
    pygame.display.update()

pygame.quit()