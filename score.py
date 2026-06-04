import pygame
from settings import *


class Score:

    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont("Arial", 24)

    def add(self, points):
        self.value += points

    def draw(self, screen):

        text = self.font.render(
            f"Score: {self.value}",
            True,
            WHITE
        )

        screen.blit(text, (10, 10))