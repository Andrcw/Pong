import pygame


class Ball():

    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def update(self):
        """Update the ship's position based on the movement flag."""

    def blitme(self):
        self.screen.blit(self.image, self.rect)