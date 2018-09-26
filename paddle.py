import pygame


class Paddle():

    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement flags for right
        self.move_right_up = False
        self.move_right_down = False

        # Movement flags for left
        self.move_left_up = False
        self.move_left_down = False

    def update(self):
        """Update the paddles's position based on the movement flag."""
        if self.move_right_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 12
        elif self.move_right_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 12
        elif self.move_left_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 12
        elif self.move_left_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 12

    def blitme(self):
        self.screen.blit(self.image, self.rect)
