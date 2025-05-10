import pygame, sys, time

import settings
from ball.Ball import Ball
from circle.Circle import Circle
from screen.Screen import Screen
from settings import WHITE


def __main__():
    pygame.init()
    screen = Screen()
    clock = pygame.time.Clock()
    circle = Circle(start_angle=0, end_angle=300)
    ball1 = Ball(color=settings.RED, vx=1, vy=2, y_offset=000)
    ball2 = Ball(color=settings.WHITE, vx=3, vy=1)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # ── Update ────────────────────────────────────────────────────────────────────
        ball1.update()
        # ball2.update()
        circle.check_collision(ball1)
        # circle.check_collision(ball2)

        # ── Clear ─────────────────────────────────────────────────────────────────────
        Screen.clear()

        # ── Draw ──────────────────────────────────────────────────────────────────────
        ball1.draw(screen)
        # ball2.draw(screen)
        circle.draw(screen)

        # ── Show ──────────────────────────────────────────────────────────────────────
        pygame.display.flip() #affiche les objects update
        clock.tick(60)

if __name__ == '__main__':
    __main__()

