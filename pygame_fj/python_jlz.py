import pygame

#创建屏幕常量
SCREEN_RECT = pygame.Rect(0,0,512,768)
#定义刷新帧数
FRAME_PER_SEC = 60
class GameSprite(pygame.sprite.Sprite):
    """飞机大战"""
    def __init__(self,image_name,speed=1):
        #调用父类
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):
    def __init__(self,is_alt=False):
        super().__init__("images/bg1.jpg")
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height