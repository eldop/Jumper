import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ground = 900
        self.cutimages()

        self.run = False
        self.bottom = [100, 100]

        self.onBlock = False
        self.onGround = False

        self.speed = [15, 0]
        self.gravity = 3
        self.up = 36
        self.ifjump = True

        # self.stayanimation()

    def update(self):

        if self.rect.bottom >= self.ground:
            self.onGround = True
            self.rect.bottom = self.ground
            self.speed[1] = 0

        else:
            self.onGround = False
            self.speed[1] += self.gravity

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.speed[0] = 15

        elif keys[pygame.K_LEFT]:
            self.speed[0] = -15

        else:
            if self.onGround == True:
                self.speed[0] = 0

        if keys[pygame.K_UP]:
            if self.onGround or self.onBlock:
                self.onBlock = False
                self.speed[0] *= 1.5
                self.speed[1] -= self.up
                print(self.onBlock)

        self.animation()
        self.rect.move_ip(self.speed)

    def cutimages(self):
        self.loadimage = pygame.image.load('speedsprite.png')
        self.runcountanimation = 0
        self.runimages = []

        self.runimages.append(self.loadimage.subsurface(30, 45, 110, 130))
        self.runimages.append(self.loadimage.subsurface(220, 45, 80, 130))
        self.runimages.append(self.loadimage.subsurface(380, 45, 90, 130))
        self.runimages.append(self.loadimage.subsurface(530, 45, 125, 130))
        self.runimages.append(self.loadimage.subsurface(695, 45, 130, 130))

        self.runimages.append(self.loadimage.subsurface(30, 215, 110, 125))
        self.runimages.append(self.loadimage.subsurface(215, 215, 80, 125))
        self.runimages.append(self.loadimage.subsurface(380, 215, 90, 130))
        self.runimages.append(self.loadimage.subsurface(540, 215, 120, 130))
        self.runimages.append(self.loadimage.subsurface(695, 45, 130, 130))

        self.jumpingsheet = pygame.image.load('jumpingsheet.png')
        self.jumpingimages = []
        self.jumpcountanimation = 0

        self.jumpingimages.append(self.jumpingsheet.subsurface(6, 30, 72, 111))
        self.jumpingimages.append(self.jumpingsheet.subsurface(93, 17, 46, 125))
        self.jumpingimages.append(self.jumpingsheet.subsurface(156, 3, 57, 136))
        self.jumpingimages.append(self.jumpingsheet.subsurface(222, 18, 69, 123))
        self.jumpingimages.append(self.jumpingsheet.subsurface(297, 14, 80, 127))
        self.jumpingimages.append(self.jumpingsheet.subsurface(395, 27, 70, 114))
        self.jumpingimages.append(self.jumpingsheet.subsurface(470, 44, 89, 97))

        self.stayingimage = pygame.image.load('stayingsheet.png')
        self.w = self.stayingimage.get_width() // 3
        self.h = self.stayingimage.get_height() // 3
        self.stayingimage = pygame.transform.scale(self.stayingimage, (self.w, self.h))
        self.myimage = self.stayingimage
        self.rect = self.myimage.get_rect()
        self.rect.bottom = self.ground

    def runanimation(self):
        self.myimage = self.runimages[self.runcountanimation]
        self.colliderect = self.myimage.get_rect()
        self.colliderect.bottom = self.rect.bottom
        if self.runcountanimation < len(self.runimages) - 1:
            self.runcountanimation += 1
        else:
            self.runcountanimation = 0

    def jumpanimation(self):
        self.myimage = self.jumpingimages[self.jumpcountanimation]
        self.colliderect = self.myimage.get_rect()
        self.colliderect.bottom = self.rect.bottom
        if self.jumpcountanimation < len(self.jumpingimages) - 1:
            self.jumpcountanimation += 1
        else:
            self.jumpcountanimation = 0

    def stayanimation(self):
        self.myimage = self.stayingimage
        self.colliderect = self.myimage.get_rect()
        self.colliderect.bottom = self.rect.bottom


    def animation(self):
        if self.speed[0] == 0 and self.speed[1] == 0 and self.onGround:
            self.stayanimation()
        else:
            if self.speed[1] != 0 or not self.onGround or not self.onBlock:
                self.jumpanimation()
            else:
                self.runanimation()

        if self.speed[0] < 0:
            self.myimage = pygame.transform.flip(self.myimage, 1, 0)
        else:
            self.myimage = self.myimage


    def checkcollide(self, blocks):
        for block in blocks.sprites():
            if block.rect.left <= self.rect.centerx <= block.rect.right:
                if self.rect.colliderect(block.rect):
                    self.onBlock = True
                    self.rect.bottom = block.rect.top + 2
                else:
                    self.onBlock = False