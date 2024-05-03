import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()  # Load player image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = 100

    def update(self, dx, dy):
        # Update player position
        self.rect.x += dx
        self.rect.y += dy
        
        # Keep player within the screen boundaries
        self.rect.x = max(0, min(self.rect.x, self.screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.screen_height - self.rect.height))

    def attack_sword(self):
        # Implement sword attack logic here
        pass

    def attack_projectile(self):
        # Implement projectile attack logic here
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
