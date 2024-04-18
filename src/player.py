import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Check if the player has reached the edge of the screen
        if self.rect.left < 0:
            self.rect.right = 520
        elif self.rect.right > 520:
            self.rect.left = 0
        elif self.rect.top < 0:
            self.rect.bottom = 520
        elif self.rect.bottom > 520:
            self.rect.top = 0
