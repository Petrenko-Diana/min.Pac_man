import pygame
from settings import *
from map_data import MAP


class Level:

    def __init__(self):
        self.map = MAP

    def draw(self, screen):

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):

                cell = self.map[row][col]

                x = col * CHAR_SIZE
                y = row * CHAR_SIZE

                if cell == '1':
                    pygame.draw.rect(
                        screen,
                        BLUE,
                        (x, y, CHAR_SIZE, CHAR_SIZE)
                    )