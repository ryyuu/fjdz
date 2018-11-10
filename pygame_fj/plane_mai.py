import pygame
from python_jlz import *


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        #1。创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2。创建游戏的时钟
        self.clock = pygame.time.Clock()
        #3。调用私有方法，精灵和精灵的创建
        self.__create_sprites()
    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1,bg2)
    def start_game(self):
        print("游戏开始....")
        while True:
            #设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #事件监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新精灵组
            self.__update_sprites()
            pygame.display.update()
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
    def __check_collide(self):
        pass
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
#if __name__ == '__main__':
game = PlaneGame()
game.start_game()