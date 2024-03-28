import pygame
import sys
import imageio

pygame.init()
X = 520
Y = 520
play = False

screen = pygame.display.set_mode((X, Y))
 
startscreenimage = imageio.mimread("images/startscreen.gif").convert()
gameplay = pygame.image.load("images/game.png").convert()


while not play:
    clock = pygame.time.Clock()
    frame_rate = 3

    frame_counter = 0
    current_frame = 0
    num_frames = len(startscreenimage)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True
    current_frame_image = pygame.image.frombuffer(startscreenimage[current_frame], (startscreenimage[current_frame].shape[1], gif_frame[current_frame].shape[0]), "RGB")
    screen.blit(current_frame_image, (0,0))
    pygame.display.flip()

    
    frame_counter += 1
    if frame_counter >= frame_rate:
        frame_counter=0
        current_frame = (current_frame + 1) % num_frames 

    clock.tick(frame_rate)

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
