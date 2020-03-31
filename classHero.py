import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.cutimages()
        self.countanimation = 0
        self.jumpcountanimation = 0

        self.stayingimage = pygame.image.load('stayingsheet.png')
        self.run = False
        self.bottom = [100, 100]
        self.w = self.stayingimage.get_width() // 3
        self.h = self.stayingimage.get_height() // 3
        self.stayingimage = pygame.transform.scale(self.stayingimage, (self.w, self.h))

        self.ground = 875
        self.onground = False

        self.speed = [15, 0]
        self.gravity = 1
        self.up = 15
        self.image = self.stayingimage
        self.rect = self.image.get_rect()
        self.ifjump = True

        #self.stayanimation()

    def update(self):
        if self.ifjump:
            self.jump()
        else:
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            #self.runanimation()
            #self.rect.bottom += self.speed[0]
            self.speed[0] = 15

        elif keys[pygame.K_LEFT]:
            #self.runanimation()
            #self.image = pygame.transform.flip(self.image, 1, 0)
            #self.bottom[0] -= self.speed[0]
            self.speed[0] = -15


        elif keys[pygame.K_UP]:
            if self.onground:
                #self.jumpanimation()
                self.jump()
        else:
            self.speed[0] = 0
            if self.onground == True:
                #self.stayanimation()
                pass




        self.bottom[1] += self.speed[1]
        if self.bottom[1] < self.ground:
            self.speed[1] += self.gravity
            self.onground = False
        else:
            self.speed[1] = 0
            self.rect.bottom = self.ground
            self.onground = True
        self.rect.move_ip(self.speed)
        #print(self.bottom)
        #print(self.rect)



    def cutimages(self):
        self.loadimage = pygame.image.load('speedsprite.png')


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

        self.jumpingimages.append(self.jumpingsheet.subsurface(6, 30, 72, 111))
        self.jumpingimages.append(self.jumpingsheet.subsurface(93, 17, 46, 125))
        self.jumpingimages.append(self.jumpingsheet.subsurface(156, 3, 57, 136))
        self.jumpingimages.append(self.jumpingsheet.subsurface(222, 18, 69, 123))
        self.jumpingimages.append(self.jumpingsheet.subsurface(297, 14, 80, 127))
        self.jumpingimages.append(self.jumpingsheet.subsurface(395, 27, 70, 114))
        self.jumpingimages.append(self.jumpingsheet.subsurface(470, 44, 89, 97))





    def runanimation(self):
        self.image = self.runimages[self.countanimation]
        self.rect = self.image.get_rect()
        self.rect.bottom = self.bottom[1]
        self.rect.centerx = self.bottom[0]
        if self.countanimation < len(self.runimages) - 1:
            self.countanimation += 1
        else:
            self.countanimation = 0





    def jumpanimation(self):
        self.image = self.jumpingimages[self.jumpcountanimation]
        self.rect = self.image.get_rect()
        self.rect.bottom = self.bottom[1]
        self.rect.centerx = self.bottom[0]
        if self.jumpcountanimation < len(self.jumpingimages) - 1:
            self.jumpcountanimation += 1
        else:
            self.jumpcountanimation = 0




    def stayanimation(self):
        self.image = self.stayingimage
        self.rect = self.image.get_rect()
        self.rect.bottom = self.bottom[1]
        self.rect.centerx = self.bottom[0]


    def jump(self):
        self.speed[0] *= 1.5
        self.speed[1] -= self.up