import pygame

from menu import Menu
from game_over import GameOver
from Game_win import GameWin

from settings import *
from level import Level
from player import Player
from berry import Berry
from score import Score
from ghost import Ghost
from HUD import HUD

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

clock = pygame.time.Clock()

menu = Menu()
game_over = GameOver()
game_win = GameWin()


def new_game():
    level = Level()
    player = Player(level)

    berries = Berry()
    score = Score()
    hud = HUD()

    ghosts = [
        Ghost(9, 9, "red", 25),
        Ghost(8, 9, "orange", 40),
        Ghost(9, 8, "cyan", 60),
        Ghost(9, 10, "pink", 80)
    ]

    return level, player, berries, score, hud, ghosts


if not menu.run(screen):
    pygame.quit()
    quit()

game_running = True

while game_running:

    level, player, berries, score, hud, ghosts = new_game()
    running = True

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_running = False

        player.move()
        player.update_power_mode()
        player.update_invincible()
        player.update_freeze()

        points = player.eat_berry(berries)
        if points:
            score.add(points)

        points = player.eat_big_berry(berries)
        if points:
            score.add(points)

        if not berries.berries and not berries.big_berries:
            if game_win.run(screen):
                running = False
            else:
                running = False
                game_running = False
            continue

        for ghost in ghosts:

            ghost.move(player)

            if player.power_mode and player.is_dead(ghost):
                ghost.reset()
                score.add(200)

            elif not player.invincible and player.is_dead(ghost):

                player.lives -= 1

                if player.lives <= 0:
                    if game_over.run(screen):
                        running = False
                    else:
                        running = False
                        game_running = False
                else:
                    player.reset()
                    player.freeze()

                break

        screen.fill(BLACK)

        level.draw(screen)
        berries.draw(screen)

        player.draw(screen)

        for ghost in ghosts:
            ghost.draw(screen, player)

        hud.draw(screen, score, player)

        pygame.display.flip()

pygame.quit()