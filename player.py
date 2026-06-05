import pygame
from settings import *
from map_data import MAP


class Player:

    def __init__(self, level):

        self.level = level
        self.lives = 3

        self.invincible = False
        self.invincible_until = 0

        self.power_mode = False
        self.power_end_time = 0

        self.move_timer = 0
        self.move_delay = PLAYER_DELAY

        self.grid_x = 1
        self.grid_y = 1

        for row in range(len(MAP)):
            for col in range(len(MAP[row])):
                if MAP[row][col] == 'P':
                    self.grid_x = col
                    self.grid_y = row
                    self.start_x = col
                    self.start_y = row
                    break

        self.pixel_x = self.grid_x * CHAR_SIZE
        self.pixel_y = self.grid_y * CHAR_SIZE

        self.frozen = False
        self.froze_until = 0

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y

        self.speed = 2
        self.radius = CHAR_SIZE // 2 - 2

    def move(self):

        if self.frozen:
            return

        now = pygame.time.get_ticks()

        keys = pygame.key.get_pressed()

        if now - self.move_timer >= self.move_delay:

            new_x = self.grid_x
            new_y = self.grid_y

            if keys[pygame.K_LEFT]:
                new_x -= 1
            elif keys[pygame.K_RIGHT]:
                new_x += 1
            elif keys[pygame.K_UP]:
                new_y -= 1
            elif keys[pygame.K_DOWN]:
                new_y += 1

            if self.can_move(new_x, new_y):
                self.grid_x = new_x
                self.grid_y = new_y

                self.target_x = new_x * CHAR_SIZE
                self.target_y = new_y * CHAR_SIZE

            self.move_timer = now

        self.update_smooth()

    def update_power_mode(self):

        if self.power_mode and pygame.time.get_ticks() >= self.power_end_time:
            self.power_mode = False

    def update_invincible(self):

        if self.invincible and pygame.time.get_ticks() >= self.invincible_until:
            self.invincible = False

    def can_move(self, gx, gy):

        if gy < 0 or gy >= len(MAP):
            return False

        if gx < 0 or gx >= len(MAP[0]):
            return False

        return MAP[gy][gx] != '1'

    def update_smooth(self):

        dx = self.target_x - self.pixel_x
        dy = self.target_y - self.pixel_y

        if dx != 0:
            self.pixel_x += 4 if dx > 0 else -4

        if dy != 0:
            self.pixel_y += 4 if dy > 0 else -4

    def draw(self, screen):

        x = self.pixel_x + CHAR_SIZE // 2
        y = self.pixel_y + CHAR_SIZE // 2

        color = WHITE if self.invincible else YELLOW

        pygame.draw.circle(
            screen,
            color,
            (x, y),
            self.radius
        )

    def get_rect(self):

        return pygame.Rect(
            self.pixel_x,
            self.pixel_y,
            CHAR_SIZE,
            CHAR_SIZE
        )

    def eat_berry(self, berries):

        pos = (self.grid_x, self.grid_y)

        if pos in berries.berries:
            berries.berries.remove(pos)
            return 10

        return 0

    def eat_big_berry(self, berries):

        pos = (self.grid_x, self.grid_y)

        if pos in berries.big_berries:
            berries.big_berries.remove(pos)

            self.power_mode = True
            self.power_end_time = pygame.time.get_ticks() + 5000

            return 50

        return 0

    def freeze(self, ms=750):

        self.frozen = True
        self.froze_until = pygame.time.get_ticks() + ms

    def update_freeze(self):

        if self.frozen and pygame.time.get_ticks() >= self.froze_until:
            self.frozen = False

    def reset(self):

        self.grid_x = self.start_x
        self.grid_y = self.start_y

        self.pixel_x = self.grid_x * CHAR_SIZE
        self.pixel_y = self.grid_y * CHAR_SIZE

        self.invincible = True
        self.invincible_until = pygame.time.get_ticks() + 2000

    def is_dead(self, ghost):
        return (self.get_rect().colliderect(ghost.get_rect()))