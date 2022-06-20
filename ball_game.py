import pygame
class Baffle:
    def __init__(self):
        self.rect = pygame.Rect((200, 400, 100, 20))
    def update(self):
        pass


class BallGame:
     # 初始化屏幕
    def __init__(self):
        # pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('弹球游戏')
        baffle = Baffle()
        pygame.draw.rect(self.screen, (255, 255, 255), [200, 400, 100, 20])

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()

    def __game_over(self):
        pygame.quit()
        exit()

    def stare_game(self):
        print('游戏kaishi')
        while True:
            self.clock.tick(60)
            self.__event_handler()
            pygame.display.update()



ball_game = BallGame()
ball_game.stare_game()

