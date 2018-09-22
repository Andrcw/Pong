import sys

import pygame


def update_screen(screen, line, right):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass of the loop.
    screen.fill((0, 0, 0))
    line.blitme()
    right.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()


def check_events(right):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_UP:
                right.moving_up = True
            elif event.key == pygame.K_DOWN:
                right.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                right.moving_up = False
            elif event.key == pygame.K_DOWN:
                right.moving_down = False
