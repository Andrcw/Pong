import sys

import pygame.sysfont
import pygame


def update_start(screen):
    screen.fill((0, 0, 0))
    title = pygame.font.SysFont("monospace", 250)
    medium = pygame.font.SysFont("monospace", 50)
    color = (255, 255, 255)
    pong = title.render("PONG", True, color)
    l_control = medium.render("Left Paddle: A and Z", True, color)
    r_control = medium.render("Right Paddle: Up and Down", True, color)
    start = medium.render("Press Space to start", True, color)
    screen.blit(pong, [135, 50])
    screen.blit(l_control, [170, 300])
    screen.blit(r_control, [170, 350])
    screen.blit(start, [170, 500])
    pygame.display.flip()


def update_screen(screen, line, right, right_top, right_bot, left, left_top, left_bot, ball):
    """Update images on the screen and flip to new screen."""
    # Connect right top and bottom paddles together
    right_bot.rect.centerx = right_top.rect.centerx
    left_bot.rect.centerx = left_top.rect.centerx

    # Redraw the screen during each pass of the loop.
    screen.fill((0, 0, 0))
    line.blitme()
    left.blitme()
    left_top.blitme()
    left_bot.blitme()
    right.blitme()
    right_top.blitme()
    right_bot.blitme()
    ball.blitme()
    score(screen, ball)
    # Make most recently drawn screen visible
    pygame.display.flip()


def check_events(right, right_top, left, left_top, ball):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_UP:
                right.move_right_up = True
            elif event.key == pygame.K_DOWN:
                right.move_right_down = True
            elif event.key == pygame.K_LEFT:
                right_top.move_player_left = True
            elif event.key == pygame.K_RIGHT:
                right_top.move_player_right = True
            elif event.key == pygame.K_SPACE:
                if ball.game_active == False:
                    ball.game_active = True
                    ball.left_score = 0
                    ball.right_score = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                right.move_right_up = False
            elif event.key == pygame.K_DOWN:
                right.move_right_down = False
            elif event.key == pygame.K_LEFT:
                right_top.move_player_left = False
            elif event.key == pygame.K_RIGHT:
                right_top.move_player_right = False


def check_ball(ball):
    # Start the ball movement
    ball.rect.centerx += ball.dx
    ball.rect.centery += ball.dy

    # IF HIT TOP
    if ball.rect.top <= ball.screen_rect.top:
        if ball.rect.right > ball.screen_rect.right / 2:
            pygame.mixer.music.load('sounds/hitwall.wav')
            pygame.mixer.music.play(0)

            # Give score to CPU, left side
            ball.rect.centerx = ball.screen_rect.centerx
            ball.rect.centery = ball.screen_rect.centery

            # Reset the ball speed and give a score
            ball.dx = ball.speed
            ball.dy = ball.speed
            ball.dx *= -1
            ball.left_score += 1

        elif ball.rect.left < ball.screen_rect.right / 2:
            pygame.mixer.music.load('sounds/hitwall.wav')
            pygame.mixer.music.play(0)

            # Give score to CPU, left side
            ball.rect.centerx = ball.screen_rect.centerx
            ball.rect.centery = ball.screen_rect.centery

            # Reset the ball speed and give a score
            ball.dx = ball.speed
            ball.dy = ball.speed
            ball.dy *= -1
            ball.right_score += 1

    # IF HIT BOTTOM
    if ball.rect.bottom >= ball.screen_rect.bottom:
        if ball.rect.right < ball.screen_rect.right / 2:
            pygame.mixer.music.load('sounds/hitwall.wav')
            pygame.mixer.music.play(0)

            # Give score to CPU, left side
            ball.rect.centerx = ball.screen_rect.centerx
            ball.rect.centery = ball.screen_rect.centery

            # Reset the ball speed and give a score
            ball.dx = ball.speed
            ball.dy = ball.speed
            ball.dy *= -1
            ball.right_score += 1

        elif ball.rect.left > ball.screen_rect.right / 2:
            # Sounds
            pygame.mixer.music.load('sounds/hitwall.wav')
            pygame.mixer.music.play(0)

            # Give score to CPU, left side
            ball.rect.centerx = ball.screen_rect.centerx
            ball.rect.centery = ball.screen_rect.centery

            # Reset the ball speed and give a score
            ball.dx = ball.speed
            ball.dy = ball.speed
            ball.dx *= -1
            ball.left_score += 1

    # If hit right side of screen, go back to middle
    if ball.rect.left >= ball.screen_rect.right:
        # Sounds
        pygame.mixer.music.load('sounds/missball.wav')
        pygame.mixer.music.play(0)

        ball.rect.centerx = ball.screen_rect.centerx
        ball.rect.centery = ball.screen_rect.centery
        # Reset the ball speed
        ball.dx = ball.speed
        ball.dy = ball.speed
        ball.dx *= -1
        ball.left_score += 1
        print("Hit right side")

    # If hit left of screen, go back to middle
    if ball.rect.right <= ball.screen_rect.left:
        # Sounds
        pygame.mixer.music.load('sounds/missball.wav')
        pygame.mixer.music.play(0)

        ball.rect.centerx = ball.screen_rect.centerx
        ball.rect.centery = ball.screen_rect.centery
        ball.dx *= -1
        ball.right_score += 1
        print("Hit LEFT")


def check_collisions(ball, right, right_top, right_bot, left, left_top, left_bot):
    # For right paddle
    # If ball collides with right paddle
    if ball.rect.colliderect(right.rect):
        # Sounds
        pygame.mixer.music.load('sounds/hitpaddle.wav')
        pygame.mixer.music.play(0)
        ball.rect.centerx -= 15
        # Make the ball speed up
        # ball.dx += .5
        # ball.dy += .5
        ball.dx *= -1

    # If ball collides with top right paddle
    if ball.rect.colliderect(right_top.rect):
        pygame.mixer.music.load('sounds/hitpaddle.wav')
        pygame.mixer.music.play(0)
        ball.dy *= -1

    # ball collide with bottom right paddle
    if ball.rect.colliderect(right_bot.rect):
        pygame.mixer.music.load('sounds/hitpaddle.wav')
        pygame.mixer.music.play(0)
        ball.dy *= -1

    # If ball collides with left paddle
    if ball.rect.colliderect(left.rect):
        # Sounds
        pygame.mixer.music.load('sounds/hitpaddle.wav')
        pygame.mixer.music.play(0)

        ball.rect.centerx += 15
        ball.dx *= -1

    # ball collide with top paddle left
    if ball.rect.colliderect(left_top.rect):
        pygame.mixer.music.load('sounds/hitpaddle.wav')
        pygame.mixer.music.play(0)
        ball.dy *= -1

    # ball collide with left bottom paddle
    if ball.rect.colliderect(left_bot.rect):
        pygame.mixer.music.load('sounds/hitpaddle.wav')
        pygame.mixer.music.play(0)
        ball.dy *= -1

def score(screen, ball):
    font = pygame.font.SysFont("monospace", 100)
    bigfont = pygame.font.SysFont("monospace", 150)
    smallfont = pygame.font.SysFont("monospace", 40)
    color = (255, 255, 255)

    left = font.render(str(ball.left_score), True, color)
    right = font.render(str(ball.right_score), True, color)

    win = bigfont.render("WIN", True, color)
    play = smallfont.render("PLAY AGAIN?", True, color)
    space = smallfont.render("(SPACEBAR)", True, color)

    screen.blit(left, [300, 10])
    screen.blit(right, [450, 10])

    if ball.left_score == 10:
        # Sounds
        pygame.mixer.music.load('sounds/win.wav')
        pygame.mixer.music.play(0)

        ball.game_active = False
        screen.blit(win, [130, 200])
        screen.blit(play, [140, 320])
        screen.blit(space, [150, 350])

    if ball.right_score == 10:
        # Sounds
        pygame.mixer.music.load('sounds/win.wav')
        pygame.mixer.music.play(0)

        ball.game_active = False
        screen.blit(win, [450, 200])
        screen.blit(play, [465, 320])
        screen.blit(space, [475, 350])