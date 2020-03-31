import pygame, classGame, classHero, classBlock

pygame.init()

game = classGame.Game()
hero = classHero.Hero()
block = classBlock.Block()











while not game.over:
    game.setFPS()
    game.background()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.over = True
    hero.update()

    game.display.blit(block.image, (block.x, block.randy))
    game.display.blit(hero.image, hero.rect)
    pygame.display.update()
pygame.quit()