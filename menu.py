import pygame

from settings import *

class Menu:
    def __init__(self):
        self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
        self.button_font = pygame.font.SysFont("Arial", 32)

        self.start_rect = pygame.Rect(
            WIDTH // 2 - 100,
            HEIGHT // 2 - 40,
            200,
            50
        )

        self.exit_rect = pygame.Rect(
            WIDTH // 2 - 100,
            HEIGHT // 2 + 40,
            200,
            50
        )

    def draw_background(self, screen):

        screen.fill(BLACK)

        # Зовнішня рамка
        pygame.draw.rect(
            screen,
            BLUE,
            (20, 20, WIDTH - 40, HEIGHT - 40),
            6
        )

        # Верхні блоки
        pygame.draw.rect(screen, BLUE, (70, 60, 140, 50), 4)
        pygame.draw.rect(screen, BLUE, (400, 60, 140, 50), 4)

        # Середні блоки
        pygame.draw.rect(screen, BLUE, (70, 180, 120, 50), 4)
        pygame.draw.rect(screen, BLUE, (420, 180, 120, 50), 4)

        # Будка привидів
        pygame.draw.rect(
            screen,
            BLUE,
            (
                WIDTH // 2 - 80,
                HEIGHT // 2 - 120,
                160,
                80
            ),
            4
        )

        # Нижні блоки
        pygame.draw.rect(screen, BLUE, (70, 500, 120, 50), 4)
        pygame.draw.rect(screen, BLUE, (420, 500, 120, 50), 4)

        # Pac-Man
        pygame.draw.circle(
            screen,
            YELLOW,
            (120, 150),
            25
        )

        # Привиди
        pygame.draw.circle(screen, RED, (420, 150), 20)
        pygame.draw.circle(screen, (255, 105, 180), (460, 150), 20)
        pygame.draw.circle(screen, (0, 255, 255), (500, 150), 20)

    def run(self, screen):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_rect.collidepoint(event.pos):
                        return True

                    if self.exit_rect.collidepoint(event.pos):
                        return False

            self.draw_background(screen)

            title = self.title_font.render(
                "PAC-MAN",
                True,
                YELLOW
            )

            screen.blit(
                title,
                (
                    (WIDTH // 2 - title.get_width() // 2) - 30,
                    120
                )
            )

            pygame.draw.rect(
                screen,
                BLUE,
                self.start_rect
            )

            pygame.draw.rect(
                screen,
                RED,
                self.exit_rect
            )

            start_text = self.button_font.render(
                "START",
                True,
                WHITE
            )

            exit_text = self.button_font.render(
                "EXIT",
                True,
                WHITE
            )

            screen.blit(
                start_text,
                (
                    self.start_rect.centerx -
                    start_text.get_width() // 2,
                    self.start_rect.centery -
                    start_text.get_height() // 2
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