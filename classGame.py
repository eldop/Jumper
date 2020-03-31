import pygame

class Game():
    def __init__(self):

        self.font = pygame.font.SysFont('DOCKER THREE', 40)

        # Display
        self.back = pygame.image.load('background.png')
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

        # Clock
        self.clock = pygame.time.Clock()
        self.FPS = 15

        self.over = False

    def setFPS(self):
        self.clock.tick(self.FPS)

    def background(self):
        self.display.blit(self.back, (0, 0))
