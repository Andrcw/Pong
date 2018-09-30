import sys

import pygame
import game_functions as gf
from line import Line
from paddle import VerticalPaddle, HorizontalPaddle, CPUVerticalPaddle, CPUHorizontalPaddle
from ball import Ball
from start import Start


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")

    # Draw line
    line = Line(screen)

    # Draw right side paddle
    right = VerticalPaddle(screen)
    right.rect.centery = right.screen_rect.centery
    right.rect.right = right.screen_rect.right

    # Draw Right top paddle
    right_top = HorizontalPaddle(screen)
    right_top.rect.top = right_top.screen_rect.top
    right_top.rect.centerx = right_top.screen_rect.centerx * 1.5

    # Draw Right bottom paddle (align to right top paddle)
    right_bot = HorizontalPaddle(screen)
    right_bot.rect.bottom = right_bot.screen_rect.bottom
    right_bot.rect.centerx = right_top.rect.centerx

    # Draw left side paddle
    left = CPUVerticalPaddle(screen)
    left.rect.centery = left.screen_rect.centery
    left.rect.left = left.screen_rect.left

    # Draw CPU top paddle
    left_top = CPUHorizontalPaddle(screen)
    left_top.rect.top = left_top.screen_rect.top
    left_top.rect.centerx = left_top.screen_rect.centerx / 2

    # Draw CPU bottom paddle
    left_bot = CPUHorizontalPaddle(screen)
    left_bot.rect.bottom = left_bot.screen_rect.bottom
    left_bot.rect.centerx = right_top.rect.centerx

    # Draw ball
    ball = Ball(screen)
    ball.rect.centerx = ball.screen_rect.centerx
    ball.rect.centery = ball.screen_rect.centery

    ball.game_active = False
    start = Start(screen)

    # Start the main loop for the game
    while True:
        gf.check_events(right, right_top, left_top, left, ball)

        if ball.start_active:
            start.start_blit(screen)
            start.start_update(left, left_top)

        if ball.game_active:
            gf.update_screen(screen, line, right, right_top, right_bot, left, left_top, left_bot, ball)
            right.update()
            right_top.update()
            left.update(ball)
            left_top.update(ball)
            ball.update()
            gf.check_ball(ball)
            gf.check_collisions(ball, right, right_top, right_bot, left, left_top, left_bot)

run_game()