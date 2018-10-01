import pygame


class VerticalPaddle:
    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/paddle_vertical.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement flags for right
        self.move_right_up = False
        self.move_right_down = False

        # Movement flags for left
        self.move_left_up = True
        self.move_left_down = True

        # Speed for paddle
        self.speed = 8

    def update(self):
        """Update the paddles's position based on the movement flag."""
        if self.move_right_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.speed
        elif self.move_right_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class HorizontalPaddle:
    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/paddle_horizontal.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement flags for right
        self.move_player_right = False
        self.move_player_left = False

        # Setting speed for the paddle movement
        self.speed = 8

    def update(self):
        """Update the paddles's position based on the movement flag."""
        # For the Player side
        if self.move_player_left and self.rect.left > self.screen_rect.right / 2:
            self.rect.centerx -= self.speed
        elif self.move_player_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class CPUVerticalPaddle:
    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/paddle_vertical.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def update(self, ball, start):
        if self.rect.centery + 10 < ball.rect.centery and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += start.speed
        elif self.rect.centery - 10 > ball.rect.centery and self.rect.top > self.screen_rect.top:
            self.rect.centery -= start.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class CPUHorizontalPaddle:
    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/paddle_horizontal.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def update(self, ball, start):
        if self.rect.centerx < ball.rect.centerx and self.rect.right < self.screen_rect.right / 2:
            self.rect.centerx += start.speed
        if self.rect.centerx > ball.rect.centerx and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= start.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
