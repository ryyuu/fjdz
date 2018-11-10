import pygame
pygame.init()
screen = pygame.display.set_mode((512,768))#返回suface

bg = pygame.image.load('images/bg1.jpg')#加载背景
#screen.blit(bg,(0,0))

hero = pygame.image.load('images/hero1.png')
#screen.blit(hero,(200,600))

#pygame.display.update()
clock = pygame.time.Clock()
#1.定义rect纪录飞机初始位置
hero_rect = pygame.Rect(200,600,128,128)
while True:

    clock.tick(50)
    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)
    pygame.display.update()

pygame.quit()