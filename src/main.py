import pygame
import sys

pygame.init()
X = 520
Y = 520
play = False

screen = pygame.display.set_mode((X, Y))
 
startscreenimage = pygame.image.load("images/startscreen.png").convert()
gameplay = pygame.image.load("images/game.png").convert()


while not play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True

    screen.blit(startscreenimage, (0, 0))
    pygame.display.flip()

    # Check for mouse click to start the game
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            play = True

# main game loop
while play:
    screen.blit(gameplay, (0, 0))
    pygame.display.flip()
    # if health == 0
        # play = False
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit()
