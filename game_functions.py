import sys

import pygame


def update_screen(screen, line, right, left, ball):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass of the loop.
    screen.fill((0, 0, 0))
    line.blitme()
    left.blitme()
    right.blitme()
    ball.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()


def check_events(right, left):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_a:
                left.move_left_up = True
            elif event.key == pygame.K_z:
                left.move_left_down = True
            elif event.key == pygame.K_UP:
                right.move_right_up = True
            elif event.key == pygame.K_DOWN:
                right.move_right_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left.move_left_up = False
            elif event.key == pygame.K_z:
                left.move_left_down = False
            elif event.key == pygame.K_UP:
                right.move_right_up = False
            elif event.key == pygame.K_DOWN:
                right.move_right_down = False

def check_ball(ball):
    ball.rect.centerx += ball.dx
    ball.rect.centery += ball.dy

    print(ball.rect.centery)

    # Border checking
    if ball.rect.top <= ball.screen_rect.top:
        ball.dy *= -1
        # print("HIT TOP!")
    if ball.rect.right >= ball.screen_rect.right:
        ball.dx *= -1
        # print("HIT RIGHT SIDE!")
    if ball.rect.bottom >= ball.screen_rect.bottom:
        ball.dy *= -1
        # print("HIT BOTTOM!")
    if ball.rect.left <= ball.screen_rect.left:
        ball.dx *= -1
        # print("HIT LEFT!")

