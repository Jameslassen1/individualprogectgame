import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = 100
        self.last_direction = pygame.Vector2(0, 0)  # Store the last movement direction

    def update(self, dx, dy):
        if dx != 0 or dy != 0:
            # Only update last direction if there's movement
            self.last_direction = pygame.Vector2(dx, dy).normalize()  # Update last movement direction
        self.rect.x += dx
        self.rect.y += dy

    def attack(self):
        # Calculate attack direction based on the player's movement direction or the last movement direction
        if self.last_direction.length() != 0:  # If player is moving
            attack_direction = self.last_direction
        else:  # If player is stationary
            attack_direction = pygame.Vector2(0, -1)  # Default attack direction (upwards)
        # Implement attack logic here based on attack_direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)
