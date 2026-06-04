import pygame
from settings import *
from map_data import MAP


class Berry:

    def __init__(self):

        self.berries = []
        self.big_berries = []

        for row in range(len(MAP)):
            for col in range(len(MAP[row])):

                if MAP[row][col] == ' ':

                    self.berries.append((col, row))

                elif MAP[row][col] == 'B':
                    self.big_berries.append((col, row))


    def draw(self, screen):

        for col, row in self.berries:

            x = col * CHAR_SIZE + CHAR_SIZE // 2
            y = row * CHAR_SIZE + CHAR_SIZE // 2

            pygame.draw.circle(
                screen,
                WHITE,
                (x, y),
                3
            )

        for col, row in self.big_berries:

            pygame.draw.circle(
                screen,
                RED,
                (
                    col * CHAR_SIZE + CHAR_SIZE // 2,
                    row * CHAR_SIZE + CHAR_SIZE //2
                ),
                8
            )
