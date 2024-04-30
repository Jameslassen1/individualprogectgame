import pygame

class Level:
    def __init__(self, background_image_path, entry_point, exit_point):
        self.background_image = pygame.image.load(background_image_path).convert()
        self.entry_point = entry_point
        self.exit_point = exit_point
        self.player = None
        self.walls = []

    def set_player(self, player):
        self.player = player
        self.player.rect.topleft = self.entry_point

    def add_wall(self, rect):
        self.walls.append(rect)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        # Do not draw walls on the screen

    def check_collision(self, rect, dx, dy):
        collision_direction = None

        for wall in self.walls:
            if rect.colliderect(wall):
                # Determine the direction of collision
                if dx > 0:  # Moving right
                    collision_direction = "right"
                elif dx < 0:  # Moving left
                    collision_direction = "left"
                elif dy > 0:  # Moving down
                    collision_direction = "down"
                elif dy < 0:  # Moving up
                    collision_direction = "up"

                return True, collision_direction

        return False, None

    def move_player_to_exit(self):
        self.player.rect.topleft = self.exit_point
