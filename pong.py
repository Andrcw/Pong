import sys

import pygame
import game_functions as gf
from line import Line
from paddle import Paddle
from ball import Ball


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
    right.rect.right = right.screen_rect.right - 40

    # Draw left paddle
    left = Paddle(screen)
    left.rect.centery = left.screen_rect.centery
    left.rect.left = left.screen_rect.left + 40

    # Draw ball
    ball = Ball(screen)
    ball.rect.centerx = ball.screen_rect.centerx
    ball.rect.centery = ball.screen_rect.centery

    # Start the main loop for the game
    while True:
        gf.check_events(right, left)
        right.update()
        left.update()
        ball.update()
        gf.update_screen(screen, line, right, left, ball)
        gf.check_ball(ball)
        gf.check_collisions(ball, right, left)

run_game()