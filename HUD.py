import pygame
from settings import WHITE


class HUD:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, screen, score, player):

        score_text = self.font.render(
            f"Score: {score.value}",
            True,
            WHITE
        )

        screen.blit(score_text, (10, 10))

        if player.power_mode:
            remaining = max(
                0,
                (player.power_end_time - pygame.time.get_ticks()) // 1000
            )

            timer_text = self.font.render(
                f"Power: {remaining}s",
                True,
                WHITE
            )

            screen.blit(timer_text, (200, 10))

        lives_text = self.font.render(
            f"Lives: {player.lives}",
            True,
            WHITE
        )

        screen.blit(lives_text, (400, 10))
