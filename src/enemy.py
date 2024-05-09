import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, screen_width, screen_height, health):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Placeholder image for the enemy
        self.image.fill((255, 0, 0))  # Red color for visibility
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = pygame.Vector2(1, 0)  # Initial movement direction (right)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = health

    def update(self, walls, player):
        # Move the enemy in its current direction
        self.rect.move_ip(self.speed * self.direction.x, self.speed * self.direction.y)
        
        # Check for collisions with walls and switch direction if needed
        for wall in walls:
            if self.rect.colliderect(wall):
                # Switch direction
                self.direction *= -1  # Reverse direction
        
        # Check for collisions with the edge of the screen and switch direction if needed
        if self.rect.left < 0 or self.rect.right > self.screen_width or \
           self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.direction *= -1  # Reverse direction
        
        # Collision detection with player
        if self.rect.colliderect(player.rect):
            player.health -= 1  # Reduce player health on collision

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Draw the enemy as a red rectangle
