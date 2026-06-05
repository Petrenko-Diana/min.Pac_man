import pygame

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

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

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

        print("YOU WIN!")
        running = False

    for ghost in ghosts:

        ghost.move(player)

        if player.power_mode and player.is_dead(ghost):

            ghost.reset()
            score.add(200)

        elif not player.invincible and player.is_dead(ghost):

            player.lives -= 1

            if player.lives <= 0:

                print("GAME OVER")
                running = False

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
