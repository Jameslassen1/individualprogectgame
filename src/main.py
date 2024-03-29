import pygame
import sys
import imageio

pygame.init()
X = 520
Y = 520
play = False

screen = pygame.display.set_mode((X, Y))
# SS means start screen
SSImage1 = pygame.image.load("images/startscreen1.png").convert()
SSImage2 = pygame.image.load("images/startscreen2.png").convert()
SSImage3 = pygame.image.load("images/startscreen3.png").convert()

gameplay = pygame.image.load("images/game.png").convert()


images = [SSImage1, SSImage2, SSImage3]

clock = pygame.time.Clock()
frame_rate = 2  # 2 frames per second

current_index = 0
num_images = len(images)
frame_duration = 1000 // frame_rate

frame_timer = 0
while not play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            play = True
    
    screen.blit(images[current_index], (0, 0))
    pygame.display.flip()

    frame_timer += clock.get_time()

    # Switch image if enough time has elapsed
    if frame_timer >= frame_duration:
        frame_timer = 0
        current_index = (current_index + 1) % num_images

    clock.tick(frame_rate)

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    screen.blit(gameplay, (0, 0))
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
