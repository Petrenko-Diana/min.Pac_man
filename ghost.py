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

            for dx, dy in [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]:

                nx = x + dx
                ny = y + dy

                if (
                    self.can_move(nx, ny)
                    and (nx, ny) not in visited
                ):

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

        for dx, dy in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]:

            nx = self.grid_x + dx
            ny = self.grid_y + dy

            if self.can_move(nx, ny):
                moves.append((nx, ny))

        if moves:
            self.grid_x, self.grid_y = random.choice(moves)

    def move(self, player):

        now = pygame.time.get_ticks()

        if now - self.move_timer < self.move_delay:
            return

        self.move_timer = now

        if random.random( ) < 0.4:

            self.random_move()

            return

        path = self.bfs(
            player.grid_x,
            player.grid_y
        )

        if path:

            next_x, next_y = path[0]

            self.grid_x = next_x
            self.grid_y = next_y

    def draw(self, screen):

        x = self.grid_x * CHAR_SIZE + CHAR_SIZE // 2
        y = self.grid_y * CHAR_SIZE + CHAR_SIZE // 2

        pygame.draw.circle(
            screen,
            self.color,
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

    def reset(self):

        self.grid_x = self.start_x
        self.grid_y = self.start_y