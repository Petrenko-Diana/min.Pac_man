import pygame

from settings import *

class GameWin:
    def __init__(self):

        self.title_font = pygame.font.SysFont(
            "Arial",
            48,
            bold=True
        )

        self.button_font = pygame.font.SysFont(
            "Arial",
            32
        )

        self.image = pygame.image.load(
            "sprites/game_win.jpg"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (250, 250)
        )

        self.restart_rect = pygame.Rect(
            WIDTH // 2 - 100,
            HEIGHT - 180,
            200,
            50
        )

        self.exit_rect = pygame.Rect(
            WIDTH // 2 - 100,
            HEIGHT - 110,
            200,
            50
        )

    def run(self, screen):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.restart_rect.collidepoint(
                            event.pos
                    ):
                        return True

                    if self.exit_rect.collidepoint(
                            event.pos
                    ):
                        return False

            screen.fill(BLACK)

            title = self.title_font.render(
                "YOU WIN!",
                True,
                YELLOW
            )

            screen.blit(
                title,
                (
                    WIDTH // 2 - title.get_width() // 2,
                    40
                )
            )

            screen.blit(
                self.image,
                (
                    WIDTH // 2 - 125,
                    120
                )
            )

            pygame.draw.rect(
                screen,
                BLUE,
                self.restart_rect
            )

            pygame.draw.rect(
                screen,
                RED,
                self.exit_rect
            )

            restart_text = self.button_font.render(
                "RESTART",
                True,
                WHITE
            )

            exit_text = self.button_font.render(
                "EXIT",
                True,
                WHITE
            )

            screen.blit(
                restart_text,
                (
                    self.restart_rect.centerx -
                    restart_text.get_width() // 2,
                    self.restart_rect.centery -
                    restart_text.get_height() // 2
                )
            )

            screen.blit(
                exit_text,
                (
                    self.exit_rect.centerx -
                    exit_text.get_width() // 2,
                    self.exit_rect.centery -
                    exit_text.get_height() // 2
                )
            )

            pygame.display.flip()