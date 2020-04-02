import pygame, classGame

pygame.init()

game = classGame.Game()

while not game.over:
    game.update()
    game.setFPS()
    game.drawing()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.over = True

pygame.quit()
