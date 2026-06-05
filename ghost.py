import random
import pygame
from collections import deque

from settings import *
from map_data import MAP


class Ghost:

    def __init__(self, row, col, color):

        self.grid_x = col
        self.grid_y = row

        self.start_x = col
        self.start_y = row

        self.pixel_x = col * CHAR_SIZE
        self.pixel_y = row * CHAR_SIZE

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y

        self.speed = 2

        self.color = pygame.Color(color)
        self.radius = CHAR_SIZE // 2 - 2

        self.move_timer = 0
        self.move_delay = GHOST_DELAY

    def can_move(self, gx, gy):

        if gy < 0 or gy >= len(MAP):
            return False

        if gx < 0 or gx >= len(MAP[0]):
            return False

        return MAP[gy][gx] != "1"

    def bfs(self, target_x, target_y):

        start = (self.grid_x, self.grid_y)
        target = (target_x, target_y)

        queue = deque([start])
        visited = {start}
        parent = {}

        while queue:

            x, y = queue.popleft()

            if (x, y) == target:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                nx = x + dx
                ny = y + dy

                if self.can_move(nx, ny) and (nx, ny) not in visited:

                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

        if start == target:
            return []

        if target not in parent:
            return []

        path = []
        current = target

        while current != start:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path

    def random_move(self):

        moves = []

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            nx = self.grid_x + dx
            ny = self.grid_y + dy

            if self.can_move(nx, ny):
                moves.append((nx, ny))

        if moves:
            nx, ny = random.choice(moves)
            self.set_target(nx, ny)

    def set_target(self, gx, gy):

        self.grid_x = gx
        self.grid_y = gy

        self.target_x = gx * CHAR_SIZE
        self.target_y = gy * CHAR_SIZE

    def move(self, player):

        now = pygame.time.get_ticks()

        if now - self.move_timer < self.move_delay:
            self.update_position()
            return

        self.move_timer = now

        # випадковість
        if random.random() < 0.4:
            self.random_move()
        else:
            path = self.bfs(player.grid_x, player.grid_y)

            if path:
                nx, ny = path[0]
                self.set_target(nx, ny)

        self.update_position()

    def update_position(self):

        dx = self.target_x - self.pixel_x
        dy = self.target_y - self.pixel_y

        if dx != 0:
            self.pixel_x += self.speed if dx > 0 else -self.speed

        if dy != 0:
            self.pixel_y += self.speed if dy > 0 else -self.speed

    def draw(self, screen):

        x = self.pixel_x + CHAR_SIZE // 2
        y = self.pixel_y + CHAR_SIZE // 2

        pygame.draw.circle(
            screen,
            self.color,
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

    def reset(self):

        self.grid_x = self.start_x
        self.grid_y = self.start_y
        self.pixel_x = self.grid_x * CHAR_SIZE
        self.pixel_y = self.grid_y * CHAR_SIZE

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y