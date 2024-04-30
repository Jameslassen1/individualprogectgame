import pygame
from player import Player
from leval import Level  # Import the Level class

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
frame_rate = 4  # 4 frames per second

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

player = Player(50, 50)

# Define Level 1 with walls around three edges and an opening for progression
level1 = Level("images/game.png", (50, 50), (750, 500))

# Set player for Level 1
level1.set_player(player)


# Format for pygame.Rect: (x-coordinate, y-coordinate, width, height)
level1.add_wall(pygame.Rect(0, 0, 520, 20))     # Top wall
level1.add_wall(pygame.Rect(0, 0, 20, 520))     # Left wall
level1.add_wall(pygame.Rect(0, 500, 520, 20))   # Bottom wall next level

current_level = level1  # Start with Level 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx = -5
    elif keys[pygame.K_RIGHT]:
        dx = 5
    elif keys[pygame.K_UP]:
        dy = -5
    elif keys[pygame.K_DOWN]:
        dy = 5

    # Collision detection
    collision, collision_direction = current_level.check_collision(player.rect, dx, dy)
    if collision:
        # If there's a collision, adjust player movement
        if collision_direction == "right" and dx > 0:
            dx = 0
        elif collision_direction == "left" and dx < 0:
            dx = 0
        elif collision_direction == "down" and dy > 0:
            dy = 0
        elif collision_direction == "up" and dy < 0:
            dy = 0

    player.update(dx,dy)

    screen.fill((0, 0, 0))  # Fill the screen with black color
    screen.blit(gameplay, (0, 0))  # Draw the gameplay screen

    current_level.draw(screen)
    screen.blit(player.image, player.rect)  # Draw the player onto the screen
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Cap the frame rate at 60 FPS

pygame.quit()
