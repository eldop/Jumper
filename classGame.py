import pygame, classBlock, classHero, map

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

        #groups
        self.blocks = pygame.sprite.Group()
        self.hero = classHero.Hero()

        self.map()

    def update(self):
        self.hero.update()
        self.blocks.update()

    def setFPS(self):
        self.clock.tick(self.FPS)


    def map(self):
        self.startx = 0
        self.starty = 0
        self.move = 256
        for line in map.lvl1:
            for symbol in line:
                if symbol == '#':
                    block = classBlock.Block(self.startx, self.starty)
                    self.blocks.add(block)
                self.startx += self.move
            self.startx = 0
            self.starty += 128

    def drawing(self):
        self.display.blit(self.back, (0, 0))
        self.display.blit(self.hero.image, self.hero.rect)
        self.blocks.draw(self.display)
        pygame.display.update()