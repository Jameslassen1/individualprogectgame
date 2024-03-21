import pygame




play = False



pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None,20)

# Main game loop
while not play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True



    pygame.display.flip()

    # Check for mouse click to start the game
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            play = True

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
