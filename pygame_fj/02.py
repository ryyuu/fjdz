import pygame
pygame.init()
screen = pygame.display.set_mode((512,768))#返回suface
bg = pygame.image.load('images/bg1.jpg')
screen.blit(bg,(0,0))
pygame.display.update()
while True:
    pass
pygame.quit()