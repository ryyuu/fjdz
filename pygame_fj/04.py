import pygame
pygame.init()
screen = pygame.display.set_mode((512,768))#返回suface

bg = pygame.image.load('images/bg1.jpg')#加载背景
screen.blit(bg,(0,0))

hero = pygame.image.load('images/hero1.png')
screen.blit(hero,(200,600))

pygame.display.update()
while True:
    pass
pygame.quit()