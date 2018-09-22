import sys

import pygame
import game_functions as gf
from line import Line
from right_paddle import Right


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")

    # Draw line
    line = Line(screen)

    # Draw right paddle
    right = Right(screen)

    # Start the main loop for the game
    while True:
        gf.check_events(right)
        right.update()
        gf.update_screen(screen, line, right)

run_game()