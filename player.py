import pygame

from settings import *
from map_data import MAP


class Player:

    def __init__(self, level):

        self.invincible = False
        self.invincible_until = 0

        self.level = level
        self.lives = 3

        self.move_timer = 0
        self.move_delay = PLAYER_DELAY

        self.power_mode = False
        self.power_end_time = 0

        self.radius = CHAR_SIZE // 2 - 2

        self.grid_x = 1
        self.grid_y = 1

        for row in range(len(MAP)):
            for col in range(len(MAP[row])):

                if MAP[row][col] == 'P':

                    self.grid_x = col
                    self.grid_y = row

                    self.start_x = col
                    self.start_y = row
                    return

    def move(self):

        now = pygame.time.get_ticks()

        if now - self.move_timer < self.move_delay:
            return

        self.move_timer = now

        keys = pygame.key.get_pressed()

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

    def update_power_mode(self):

        if (
            self.power_mode and
            pygame.time.get_ticks() >= self.power_end_time
        ):
            self.power_mode = False

    def update_invincible(self):

        if (
                self.invincible and
                pygame.time.get_ticks() >= self.invincible_until
        ):
            self.invincible = False

    def can_move(self, gx, gy):

        if gy < 0 or gy >= len(MAP):
            return False

        if gx < 0 or gx >= len(MAP[0]):
            return False

        return MAP[gy][gx] != '1'

    def draw(self, screen):

        x = self.grid_x * CHAR_SIZE + CHAR_SIZE // 2
        y = self.grid_y * CHAR_SIZE + CHAR_SIZE // 2

        color = YELLOW

        if self.invincible:
            color = WHITE

        pygame.draw.circle(
            screen,
            color,
            (x, y),
            self.radius
        )

    def get_rect(self):

        return pygame.Rect(
            self.grid_x * CHAR_SIZE,
            self.grid_y * CHAR_SIZE,
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
            self.power_end_time = pygame.time.get_ticks() + 8000

            return 50

        return 0

    def reset(self):

        self.grid_x = self.start_x
        self.grid_y = self.start_y

        self.invincible = True
        self.invincible_until = pygame.time.get_ticks() + 2000

    def is_dead(self, ghost):

        return (
            self.grid_x == ghost.grid_x and
            self.grid_y == ghost.grid_y
        )
