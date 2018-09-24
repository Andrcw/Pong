import pygame


class Ball():

    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # speed
        self.dx = 10
        self.dy = 10

    def update(self):
        """Idk"""

    def blitme(self):
        self.screen.blit(self.image, self.rect)