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


level1 = Level("images/leval1.png", (50, 50), (750, 500))
level1.set_player(player)
level1.add_wall(pygame.Rect(0, 0, 520, 20))     
level1.add_wall(pygame.Rect(0, 0, 20, 520))    
level1.add_wall(pygame.Rect(0, 500, 520, 20))
level1.add_wall(pygame.Rect(100, 200, 50, 50))

level2 = Level("images/leval2.png", (50, 50), (750, 500))
level2.add_wall(pygame.Rect(0, 0, 520, 20))     
level2.add_wall(pygame.Rect(0, 0, 20, 520))    
level2.add_wall(pygame.Rect(0, 500, 520, 20))
level2.add_wall(pygame.Rect(100, 200, 50, 50))


# Format for pygame.Rect: (x-coordinate, y-coordinate, width, height)


current_level = level1  # Start with Level 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx = -3
    elif keys[pygame.K_RIGHT]:
        dx = 3
    elif keys[pygame.K_UP]:
        dy = -3
    elif keys[pygame.K_DOWN]:
        dy = 3

    # Collision detection
    collision, collision_direction = current_level.check_collision(player.rect, dx, dy)
    if collision:
        # If there's a collision, adjust player movement
        if collision_direction == "right" and dx > 0:
            dx = -20
        elif collision_direction == "left" and dx < 0:
            dx = +20
        elif collision_direction == "down" and dy > 0:
            dy = -20
        elif collision_direction == "up" and dy < 0:
            dy = +20

    player.update(dx,dy)

    # Check if player reached the edge of the screen
    if player.rect.left < 0 or player.rect.right > X or player.rect.top < 0 or player.rect.bottom > Y:
        # Move to the next level
        if current_level == level1:
            current_level = level2
        else:
            # Here you can add more levels or any other action you want
            pass
        player.rect.topleft = current_level.entry_point

    screen.fill((0, 0, 0))  
    
    for wall in current_level.walls:
        pygame.draw.rect(screen, (255, 255, 255), wall)

    current_level.draw(screen)
    screen.blit(player.image, player.rect)  
    pygame.display.flip()  

    clock.tick(60)  

pygame.quit()
