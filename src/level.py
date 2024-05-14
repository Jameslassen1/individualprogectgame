import pygame

class Level:
    def __init__(self, background_image_path, entry_point, exit_point):
        self.background_image = pygame.image.load(background_image_path).convert()
        self.entry_point = entry_point
        self.exit_point = exit_point
        self.player = None
        self.walls = []
        self.enemies = pygame.sprite.Group()  # Create a sprite group for enemies

    def set_player(self, player):
        self.player = player
        self.player.rect.topleft = self.entry_point

    def add_wall(self, rect):
        self.walls.append(rect)

    def add_enemy(self, enemy):
        self.enemies.add(enemy)  # Add enemy to the sprite group

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, (255, 255, 255), wall)

        # Draw enemies
        self.enemies.draw(screen)

        # Draw player
        screen.blit(self.player.image, self.player.rect)

    def update_enemies(self):
        self.enemies.update()

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
