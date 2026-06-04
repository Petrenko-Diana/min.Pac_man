import pygame
from settings import WHITE


class HUD:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, screen, score, player):

        # SCORE
        score_text = self.font.render(
            f"Score: {score.value}",
            True,
            WHITE
        )

        screen.blit(score_text, (10, 10))