import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png").convert_alpha()  # Load enemy image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = direction
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = 100

    def update(self):
        # Update enemy position based on its direction and speed
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        # Keep enemy within the screen boundaries
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.direction = (-self.direction[0], self.direction[1])
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.direction = (self.direction[0], -self.direction[1])

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Remove the enemy from the sprite group when its health reaches 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
