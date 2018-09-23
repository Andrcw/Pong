import sys

import pygame
import game_functions as gf
from line import Line
from paddle import Paddle


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")

    # Draw line
    line = Line(screen)

    # Draw right paddle
    right = Paddle(screen)
    right.rect.centery = right.screen_rect.centery
    right.rect.right = right.screen_rect.right - 20

    # Draw left paddle
    left = Paddle(screen)
    left.rect.centery = left.screen_rect.centery
    left.rect.left = left.screen_rect.left + 20

    # Start the main loop for the game
    while True:
        gf.check_events(right, left)
        right.update()
        left.update()
        gf.update_screen(screen, line, right, left)

run_game()