import pygame, random

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('block.png')
        self.rect = self.image.get_rect()
        self.randy = random.randint(600, 800)
        self.x = 760


    def update(self):
        pass